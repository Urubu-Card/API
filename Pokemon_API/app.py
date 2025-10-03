import streamlit as st
import requests
from deep_translator  import GoogleTranslator



def traduzir_texto(texto,linguagem='pt'):
    traducao = GoogleTranslator(source='en',target=linguagem).translate(texto)
    return traducao





@st.cache_resource
def busca(url):
    """
!---   Faz a busca simples indo a busca da url entregando a resposta em JSON ---!
    """

    try:
        resposta = requests.get(url=url)

        dados = resposta.json()

        

        return dados
    
    except requests.exceptions.JSONDecodeError:

        erro =True
        return erro



def falar_caracteristicas(dados):
    col1,col2 = st.columns(2)

    with col1:
#TODO           Nome do Pokemon :
        st.title(f"{dados['name'].capitalize()} : ")

#TODO           ID do Pokemon :
        st.subheader(f"Número da Pokedex : {dados['id']}")
                
#TODO           Tipos do Pokemon :
        st.markdown("### **Tipos do Pokemon** :")
        for tipos in dados['types']:
            
            url_tipo = (tipos['type']['url'])
            
            dado_tipos = busca(url_tipo)

            st.image(dado_tipos['sprites']['generation-viii']['brilliant-diamond-and-shining-pearl']['name_icon'],clamp=0)

#TODO           Atributos Peso e Altura :

        altura = int(dados['height'])/10

        st.markdown(f"#### Altura : {altura}m")

        peso = int(dados['weight']) /10
        
        st.markdown(f"#### Peso : {peso}kg")



        with st.expander("Habilidades :"):
            for habilidades in dados['abilities']:

                    buscar_habil =busca(habilidades['ability']['url'])

                    
                    st.markdown(f"##### {traduzir_texto(buscar_habil['name']).capitalize()} : ")


    with col2:
        imagem = st.image(dados['sprites']['other']['official-artwork']['front_default'])

        #! Fazer uma coisa para se tiver outras imgaens in ['other'] mudar a variavel pra mostrar outra imgaem
        



def main():
    nome_poke = st.text_input("Digite o nome de um pokemon",placeholder="Ex: Gengar")


    if st.button("Realizar Busca : "):
        
        if not nome_poke :
            st.error("⚠️ Nome do Pokémon não inserido !")

        else:

            
            url = f"https://pokeapi.co/api/v2/pokemon/{nome_poke}"
            
            dados =busca(url)
            
            if dados ==True:
                st.error("Erro : Pokemon não encontrado !")
            
            else:
            
                with st.container():
                    falar_caracteristicas(dados)

if __name__ =='__main__':
    main()
            
