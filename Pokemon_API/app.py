import streamlit as st
import requests




@st.cache_resource
def busca(url):
    """
!---   Faz a busca simples indo a busca da url entregando a resposta em JSON ---!
    """
    
    resposta = requests.get(url=url)
    
    dados = resposta.json()
    
    return dados


nome_poke = st.text_input("Digite o nome de um pokemon",placeholder="Ex: Gengar")


if st.button("Realizar Busca : "):
    
    url = f"https://pokeapi.co/api/v2/pokemon/{nome_poke}"
    
    dados =busca(url)
    
    with st.container():
        col1,col2 = st.columns(2)
        
        with col1:
            st.title(dados['name'].capitalize())

            st.subheader(f"ID do Pokemon : {dados['id']}")
            
            
            for tipos in dados['types']:
                
                st.markdown(f"#### -**{tipos['type']['name'].capitalize()}**")
                
                url_tipo = (tipos['type']['url'])
                
                dado_tipos = busca(url_tipo)
                
                st.write(dado_tipos['names'])
                
                
                for tipo_real in dado_tipos['names']:
                    
                    st.write(tipo_real['language'])
                    if 'es' in tipo_real['language']['name']:
                        
                        st.write(tipo_real['language'])
                        
                    
        
        with col2:
            st.image(dados['sprites']['other']['showdown']['front_default'],width=500)
    