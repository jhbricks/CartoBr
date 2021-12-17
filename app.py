#Importa bibliotecas
import streamlit as st
import folium
import streamlit_folium
from streamlit_folium import folium_static


#Layout da página
name = "Cartografia do Brasil através dos anos"
st.set_page_config(layout="wide", page_title=name)

#Opções do menu
st.sidebar.markdown('# Cartografia do Brasil através dos anos')
options = st.sidebar.selectbox("Selecione uma opção:", ("Linha do tempo: 1900 - 1990", "Linha do tempo com mapas históricos","Mapas históricos"))


#Configuração do basemap
bmurl = 'http://server.arcgisonline.com/ArcGIS/rest/services/'
bm = 'NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}'
natgeo = bmurl + bm
#Estilos dos contornos e dos preenchimentos
style = {'fillColor': '#FF000000', 'color': 'black'}
style1 = {'fillColor': 'red', 'color': 'red'}

#Links dos arquivos
#Arquivos geojson
m1872 = 'https://raw.githubusercontent.com/jhbricks/Dados/main/1872.geojson'
m1900 = 'https://raw.githubusercontent.com/jhbricks/Dados/main/1900.geojson'
m1910 = 'https://raw.githubusercontent.com/jhbricks/Dados/main/1910.geojson'
m1920 = 'https://raw.githubusercontent.com/jhbricks/Dados/main/1920.geojson'
m1930 = 'https://raw.githubusercontent.com/jhbricks/Dados/main/1930.geojson'
m1940 = 'https://raw.githubusercontent.com/jhbricks/Dados/main/1940.geojson'
n1940 = 'https://raw.githubusercontent.com/jhbricks/Dados/main/novos1940.geojson'
m1950 = 'https://raw.githubusercontent.com/jhbricks/Dados/main/1950.geojson'
m1960 = 'https://raw.githubusercontent.com/jhbricks/Dados/main/1960.geojson'
n1960 = 'https://raw.githubusercontent.com/jhbricks/Dados/main/novos1960.geojson'
m1970 = 'https://raw.githubusercontent.com/jhbricks/Dados/main/1970.geojson'
m1980 = 'https://raw.githubusercontent.com/jhbricks/Dados/main/1980.geojson'
n1980 = 'https://raw.githubusercontent.com/jhbricks/Dados/main/novos1980.geojson'
m1990 = 'https://raw.githubusercontent.com/jhbricks/Dados/main/1990.geojson'
n1990 = 'https://raw.githubusercontent.com/jhbricks/Dados/main/novos1990.geojson'
#Imagens dos mapas
i1870 = "https://tile.loc.gov/image-services/iiif/service:gmd:gmd5:g5400:g5400:br000023/full/pct:25/0/default.jpg"
i1900 = "https://tile.loc.gov/image-services/iiif/service:gmd:gmd5:g5400:g5400:ct000637/full/pct:12.5/0/default.jpg"
i1910 = "https://tile.loc.gov/image-services/iiif/service:gmd:gmd5:g5401:g5401p:br000060/full/pct:12.5/0/default.jpg"
i1920 = "http://www.mapas-historicos.com/atlas-1923/imagens/mapa-brasil-antigo.jpg"
i1930 = "https://raw.githubusercontent.com/jhbricks/Dados_capitais/main/1930.jpg"
i1940 = "https://biblioteca.ibge.gov.br/visualizacao/mapas/GEBIS%20-%20RJ/map6583.jpg"
i1950 = "https://biblioteca.ibge.gov.br/visualizacao/mapas/GEBIS%20-%20RJ/map6050.jpg"
i1960 = "https://biblioteca.ibge.gov.br/visualizacao/mapas/GEBIS%20-%20RJ/map6052.jpg"
i1970 = "https://www.historia-brasil.com/mapas/mapa/brasil-seculo20.jpg"
i1980 = "https://www.historia-brasil.com/mapas/mapa/brasil-seculo20.jpg"
i1990 = "https://biblioteca.ibge.gov.br/visualizacao/mapas/GEBIS%20-%20RJ/map6528.jpg"
#Fonte dos shapefiles
ibge = '[IBGE] (https://www.ibge.gov.br/geociencias/organizacao-do-territorio/estrutura-territorial/15771-evolucao-da-divisao-territorial-do-brasil.html?=&t=downloads)'

#Timeline: Divisão com mapas históricos

if options == "Linha do tempo com mapas históricos":
  st.subheader("Linha do tempo com mapas históricos")
  st.sidebar.markdown("**Dica:** Feche este menu para uma melhor visualização dos mapas.")
  st.sidebar.markdown("Escolha uma década pela aba ***“Selecione um período”***.")
  st.sidebar.markdown("No mapa interativo (à esquerda) é possível verificar o nome dos estados passando o mouse em cima. Quando houver alguma modificação na divisão territorial em relação com a década anterior a mesma estará em destaque na cor vermelha e abaixo do mapa haverá uma descrição da alteração.")
  st.sidebar.markdown("O mapa à direita é o mapa histórico, ou seja, o mapa elaborado naquela respectiva década.")
  st.sidebar.markdown("Obs.: Alguns mapas podem demorar um pouco para carregar.")
  st.sidebar.markdown("Abaixo dos mapas estão as suas respectivas fontes, clique no link caso queira visualiza-los com mais detalhes.")


  periodo = st.selectbox('Selecione um período', (1870, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990))

#Escolha do período 1870
  if periodo == 1870:
    st.header("Década de 1870")
    col1, col2 = st.columns(2)
#Coluna 1: Mapa Interativo 1870
    with col1:
      m = folium.Map (location = [-15,-53], tiles=natgeo, attr='National Geographic, Esri',zoom_start =  4)   
      folium.GeoJson(m1872, name='1872', tooltip=folium.GeoJsonTooltip(fields=['nome']),
                     style_function=lambda x: {'fillColor': '#FF000000','color':'black'} 
      ).add_to(m)
      folium_static(m, width=500, height=550)
      #Texto e fonte
      with st.expander("Fonte:"):
        st.write("Divisão Territorial 1872 - 1990. Evolução da Divisão Territorial do Brasil. Rio de Janeiro: IBGE, [2010].")
        st.write('Disponível em:', ibge, unsafe_allow_html=True)      
#Coluna 2: Mapa histórico 1870
    with col2:
      st.image(i1870, width=500)
      st.markdown("**Colton's Brazil with Guayana**")
      st.markdown("Ano: 1871")
      with st.expander("Fonte:"):
        st.write("G.W. & C.B. Colton & Co. Colton's Brazil with Guayana. 1871")  
        link = '[Library of Congress](https://www.loc.gov/item/2003627063/)'
        st.write('Disponível em:', link, unsafe_allow_html=True)

#Escolha do período 1900
  elif periodo == 1900:
    st.header("Década de 1900")
    col1, col2 = st.columns(2)
#Coluna 1: Mapa Interativo 1900
    with col1:
      m = folium.Map (location = [-15,-53], tiles=natgeo, attr='National Geographic, Esri',zoom_start =  4)   
      folium.GeoJson(m1900, name='1900', tooltip=folium.GeoJsonTooltip(fields=['nome']),
                     style_function=lambda x: style 
      ).add_to(m)
      folium_static(m, width=500, height=550)
      #Texto e fonte
      with st.expander("Fonte:"):
        st.write("Divisão Territorial 1872 - 1990. Evolução da Divisão Territorial do Brasil. Rio de Janeiro: IBGE, [2010].")
        st.write('Disponível em:', ibge, unsafe_allow_html=True)        
#Coluna 2: Mapa histórico 1900
    with col2:
      st.image(i1900, use_column_width = True)
      st.markdown("**Mappa geral da Republica dos Estados Unidos do Brasil**")
      st.markdown("Ano: 1908")
      with st.expander("Fonte:"):
        st.write("International Bureau Of The American Republics. Brazil: From Official and Other Sources. dir by Fox, Williams C.Ector [Washington, DC: International Bureau of the American Republics, 1905] ")  
        link = '[Library of Congress](https://www.loc.gov/item/2012593200/)'
        st.write('Disponível em:', link, unsafe_allow_html=True)

#Escolha do período 1910
  elif periodo == 1910:
    st.header("Década de 1910")
    col1, col2 = st.columns(2)
#Coluna 1: Mapa Interativo 1910
    with col1:
      m = folium.Map (location = [-15,-53], tiles=natgeo, attr='National Geographic, Esri',zoom_start =  4)   
      folium.GeoJson(m1910, name='1910', tooltip=folium.GeoJsonTooltip(fields=['nome']),
                     style_function=lambda x: style1
                                              if x['properties']['nome']=='Território do Acre'
                                              else style 
      ).add_to(m)
      folium_static(m, width=500, height=550)
      #Texto e fonte
      st.markdown("**Alteração na divisão territorial na década de 1910: **")
      st.markdown("Acre foi incorporado ao Brasil em 1911 como Território do Acre.")
      with st.expander("Fonte:"):
        st.write("Divisão Territorial 1872 - 1990. Evolução da Divisão Territorial do Brasil. Rio de Janeiro: IBGE, [2010].")
        st.write('Disponível em:', ibge, unsafe_allow_html=True)
#Coluna 2: Mapa histórico 1910
    with col2:
      st.image(i1910, use_column_width = True)
      st.markdown("**Carta da viação ferrea do Brasil**")
      st.markdown("Ano: 1913")
      with st.expander("Fonte:"):
        st.write("Cunha, E. A. L.; Calmon, M.; Gama, A.; Dilermando e Luiz, E.; Roosevelt, B; Roosevelt, T. Carta da viação ferrea do Brasil. São Paulo: Secção Geographica Artistica da Compa. Lith. Hartmann-Reichenbach, 1910")  
        link = '[Library of Congress](https://www.loc.gov/resource/g5401p.br000060/)'
        st.write('Disponível em:', link, unsafe_allow_html=True)

#Escolha do período 1920
  elif periodo == 1920:
    st.header("Década de 1920")
    col1, col2 = st.columns(2)
#Coluna 1: Mapa Interativo 1920
    with col1:
      m = folium.Map (location = [-15,-53], tiles=natgeo, attr='National Geographic, Esri',zoom_start =  4)   
      folium.GeoJson(m1920, name='1920', tooltip=folium.GeoJsonTooltip(fields=['nome']),
                     style_function=lambda x: style1
                                              if x['properties']['nome']=='Santa Catharina'
                                              else style 
      ).add_to(m)
      folium_static(m, width=500, height=550)
      #Texto e fonte
      st.markdown("**Alteração na divisão territorial na década de 1920: **")
      st.markdown("O Estado de Santa Catarina (Catharina) modificou para seu formato atual no final da década.")
      with st.expander("Fonte:"):
        st.write("Divisão Territorial 1872 - 1990. Evolução da Divisão Territorial do Brasil. Rio de Janeiro: IBGE, [2010].")
        st.write('Disponível em:', ibge, unsafe_allow_html=True)
#Coluna 2: Mapa histórico 1920
    with col2:
      st.image(i1920, use_column_width = True)
      st.markdown("**Carta política do Brasil**")
      st.markdown("Ano: 1923")
      with st.expander("Fonte:"):
        st.write("Mello, H. Carta política do Brasil. Geographia-Atlas do Brasil e das cinco partes do mundo. F. Briguiet & Cia, 1923.")
        link = '[Mapas Históricos](http://www.mapas-historicos.com/atlas-1923/brasil.htm/)'
        st.write('Disponível em:', link, unsafe_allow_html=True)

#Escolha do período 1930
  elif periodo == 1930:
    st.header("Década de 1930")
    col1, col2 = st.columns(2)
#Coluna 1: Mapa Interativo 1930
    with col1:
      m = folium.Map (location = [-15,-53], tiles=natgeo, attr='National Geographic, Esri',zoom_start =  4)   
      folium.GeoJson(m1930, name='1930', tooltip=folium.GeoJsonTooltip(fields=['nome']),
                     style_function=lambda x: style 
      ).add_to(m)
      folium_static(m, width=500, height=550)
      #Texto e fonte
      with st.expander("Fonte:"):
        st.write("Divisão Territorial 1872 - 1990. Evolução da Divisão Territorial do Brasil. Rio de Janeiro: IBGE, [2010].")
        st.write('Disponível em:', ibge, unsafe_allow_html=True)        
#Coluna 2: Mapa histórico 1930 
    with col2:
      st.image(i1930, use_column_width = True)
      st.markdown("**Südamerika, Staatenkarte**")
      st.markdown("Ano: 1931")
      with st.expander("Fonte:"):
        st.write("Diercke, C. Südamerika, Staatenkarte. George Westermann, Diercke Schulatlas Für Höhere Lehranstalten, 1931.")  
        link = '[Alabama Maps](https://tinyurl.com/y35xj58a)'
        st.write('Disponível em:', link, unsafe_allow_html=True)

#Escolha do período 1940
  elif periodo == 1940:
    st.header("Década de 1940")
    col1, col2 = st.columns(2)
#Coluna 1: Mapa Interativo 1940
    with col1:
      m = folium.Map (location = [-15,-53], tiles=natgeo, attr='National Geographic, Esri',zoom_start =  4)   
      folium.GeoJson(m1940, name='1940', tooltip=folium.GeoJsonTooltip(fields=['nome']),
                     style_function=lambda x: style).add_to(m)
      folium.GeoJson(n1940, name='1940', tooltip=folium.GeoJsonTooltip(fields=['nome']),
                     style_function=lambda x: style1).add_to(m)
      folium_static(m, width=500, height=550)
      #Texto e fonte
      st.markdown("**Alteração na divisão territorial na década de 1940: **")
      st.markdown("Foram criados os territórios federais de Guaporé,  Rio Branco, Amapá, Fernando de Noronha, Iguassú e Ponta Porã em 1943.")
      with st.expander("Fonte:"):
        st.write("Divisão Territorial 1872 - 1990. Evolução da Divisão Territorial do Brasil. Rio de Janeiro: IBGE, [2010].")
        st.write('Disponível em:', ibge, unsafe_allow_html=True)        
#Coluna 2: Mapa histórico 1940 
    with col2:
      st.image(i1940, use_column_width = True)
      st.markdown("**Mapa do Brasil**")
      st.markdown("Ano: 1940")
      with st.expander("Fonte:"):
        st.write("Mapa do Brasil. Rio de Janeiro: IBGE, [1940]")  
        link = '[IBGE](https://biblioteca.ibge.gov.br/index.php/biblioteca-catalogo?view=detalhes&id=66583)'
        st.write('Disponível em:', link, unsafe_allow_html=True)

#Escolha do período 1950
  elif periodo == 1950:
    st.header("Década de 1950")
    col1, col2 = st.columns(2)
#Coluna 1: Mapa Interativo 1950
    with col1:
      m = folium.Map (location = [-15,-53], tiles=natgeo, attr='National Geographic, Esri',zoom_start =  4)   
      folium.GeoJson(m1950, name='1950', tooltip=folium.GeoJsonTooltip(fields=['nome']),
                     style_function=lambda x: style
      ).add_to(m)
      folium_static(m, width=500, height=550)
      #Texto e fonte
      with st.expander("Fonte:"):
        st.write("Divisão Territorial 1872 - 1990. Evolução da Divisão Territorial do Brasil. Rio de Janeiro: IBGE, [2010].")
        st.write('Disponível em:', ibge, unsafe_allow_html=True)
#Coluna 2: Mapa histórico 1950
    with col2:
      st.image(i1950, use_column_width = True)
      st.markdown("**Mapa do Brasil**")
      st.markdown("Ano: 1950")
      with st.expander("Fonte:"):
        st.write("Mapa do Brasil. Rio de Janeiro: IBGE, [1950]")
        link = '[IBGE](https://biblioteca.ibge.gov.br/index.php/biblioteca-catalogo?view=detalhes&id=66050)'
        st.write('Disponível em:', link, unsafe_allow_html=True)

#Escolha do período 1960
  elif periodo == 1960:
    st.header("Década de 1960")
    col1, col2 = st.columns(2)
#Coluna 1: Mapa Interativo 1960
    with col1:
      m = folium.Map (location = [-15,-53], tiles=natgeo, attr='National Geographic, Esri',zoom_start =  4)   
      folium.GeoJson(m1960, name='1960', tooltip=folium.GeoJsonTooltip(fields=['nome']),
                     style_function=lambda x: style).add_to(m)
      folium.GeoJson(n1960, name='1960', tooltip=folium.GeoJsonTooltip(fields=['nome']),
                     style_function=lambda x: style1).add_to(m)
      folium_static(m, width=500, height=550)
      #Texto e fonte
      st.markdown("**Alteração na divisão territorial na década de 1960: **")
      st.markdown("Os territórios de Guaporé e de Rio Branco passaram a ser denominados de Rondônia e Roraima, respectivamente. A capital do país foi transferida para Brasília e o antigo distrito federal tornou-se o Estado da Guanabara. .")
      with st.expander("Fonte:"):
        st.write("Divisão Territorial 1872 - 1990. Evolução da Divisão Territorial do Brasil. Rio de Janeiro: IBGE, [2010].")
        st.write('Disponível em:', ibge, unsafe_allow_html=True)        
#Coluna 2: Mapa histórico 1960 
    with col2:
      st.image(i1960, use_column_width = True)
      st.markdown("**Mapa do Brasil**")
      st.markdown("Ano: 1960")
      with st.expander("Fonte:"):
        st.write("Mapa do Brasil. Rio de Janeiro: IBGE, [1960]")  
        link = '[IBGE](https://biblioteca.ibge.gov.br/index.php/biblioteca-catalogo?view=detalhes&id=66052)'
        st.write('Disponível em:', link, unsafe_allow_html=True)

#Escolha do período 1970
  elif periodo == 1970:
    st.header("Década de 1970")
    col1, col2 = st.columns(2)
#Coluna 1: Mapa Interativo 1970
    with col1:
      m = folium.Map (location = [-15,-53], tiles=natgeo, attr='National Geographic, Esri',zoom_start =  4)   
      folium.GeoJson(m1970, name='1970', tooltip=folium.GeoJsonTooltip(fields=['nome']),
                     style_function=lambda x: style1
                                              if x['properties']['nome']=='Acre'
                                              else style 
      ).add_to(m)
      folium_static(m, width=500, height=550)
      #Texto e fonte
      st.markdown("**Alteração na divisão territorial na década de 1970: **")
      st.markdown("Território do Acre foi categorizado como estado.")
      with st.expander("Fonte:"):
        st.write("Divisão Territorial 1872 - 1990. Evolução da Divisão Territorial do Brasil. Rio de Janeiro: IBGE, [2010].")
        st.write('Disponível em:', ibge, unsafe_allow_html=True)
#Coluna 2: Mapa histórico 1970
    with col2:
      st.image(i1970, use_column_width = True)
      st.markdown("**Mapa do Brasil**")
      st.markdown("Ano: 1979")
      with st.expander("Fonte:"):
        st.write("Barbosa, R.P. Mapa do Brasil. Dicionário Enciclopédico Koogan Larousse Seleções, 1979")  
        link = '[Mapas Históricos](https://www.historia-brasil.com/mapas/seculo-20.htm)'
        st.write('Disponível em:', link, unsafe_allow_html=True)

#Escolha do período 1980
  elif periodo == 1980:
    st.header("Década de 1980")
    col1, col2 = st.columns(2)
#Coluna 1: Mapa Interativo 1980 
    with col1:
      m = folium.Map (location = [-15,-53], tiles=natgeo, attr='National Geographic, Esri',zoom_start =  4)   
      folium.GeoJson(m1980, name='1980', tooltip=folium.GeoJsonTooltip(fields=['nome']),
                     style_function=lambda x: style).add_to(m)
      folium.GeoJson(n1980, name='1980', tooltip=folium.GeoJsonTooltip(fields=['nome']),
                     style_function=lambda x: style1).add_to(m)
      folium_static(m, width=500, height=550)
      #Texto e fonte
      st.markdown("**Alteração na divisão territorial na década de 1980: **")
      st.markdown("Mato Grosso foi dividido em Mato Grosso e Mato Grosso do Sul. O estado de Guanabara fundiu-se com Rio de Janeiro. Em 1988, Goiás foi dividido em Goiás e Tocantinhas. Rondônia foi categorizado como estado em 1982.")
      with st.expander("Fonte:"):
        st.write("Divisão Territorial 1872 - 1990. Evolução da Divisão Territorial do Brasil. Rio de Janeiro: IBGE, [2010].")
        st.write('Disponível em:', ibge, unsafe_allow_html=True)        
#Coluna 2: Mapa histórico 1980 
    with col2:
      st.image(i1980, use_column_width = True)
      st.markdown("**Mapa do Brasil**")
      st.markdown("Ano: 1979")
      with st.expander("Fonte:"):
        st.write("Barbosa, R.P. Mapa do Brasil. Dicionário Enciclopédico Koogan Larousse Seleções, 1979")  
        link = '[Mapas Históricos](https://www.historia-brasil.com/mapas/seculo-20.htm)'
        st.write('Disponível em:', link, unsafe_allow_html=True)

#Escolha do período 1990
  elif periodo == 1990:
    st.header("Década de 1990")
    col1, col2 = st.columns(2)
#Coluna 1: Mapa Interativo 1990
    with col1:
      m = folium.Map (location = [-15,-53], tiles=natgeo, attr='National Geographic, Esri',zoom_start =  4)   
      folium.GeoJson(m1990, name='1990', tooltip=folium.GeoJsonTooltip(fields=['nome']),
                     style_function=lambda x: style).add_to(m)
      folium.GeoJson(n1990, name='1990', tooltip=folium.GeoJsonTooltip(fields=['nome']),
                     style_function=lambda x: style1).add_to(m)
      folium_static(m, width=500, height=550)
      #Texto e fonte
      st.markdown("**Alteração na divisão territorial na década de 1990: **")
      st.markdown("Fernando de Noronha foi agregado ao estado de Pernambuco. Roraima, Rondônia e Amapá foram categorizados como estado.")
      with st.expander("Fonte:"):
        st.write("Divisão Territorial 1872 - 1990. Evolução da Divisão Territorial do Brasil. Rio de Janeiro: IBGE, [2010].")
        st.write('Disponível em:', ibge, unsafe_allow_html=True)        
#Coluna 2: Mapa histórico 1990
    with col2:
      st.image(i1990, use_column_width = True)
      st.markdown("**República Federativa do Brasil: Mapa escolar**")
      st.markdown("Ano: 1990")
      with st.expander("Fonte:"):
        st.write(" República Federativa do Brasil: Mapa escolar. Rio de Janeiro: IBGE, [1990]")  
        link = '[IBGE](https://biblioteca.ibge.gov.br/index.php/biblioteca-catalogo?view=detalhes&id=66528)'
        st.write('Disponível em:', link, unsafe_allow_html=True)


#Timeline
elif options == "Linha do tempo: 1900 - 1990":
  st.sidebar.markdown("Escolha uma década deslizando o cursor no slider ***“Selecione um período”*** e veja as divisões territoriais através das décadas do século XX.")
  st.subheader("Linha do tempo: 1900 - 1990")
  choose = st.slider('Selecione um período:', min_value=1900, max_value=1990, step = 10)
#Início do código do mapa
  c1, c2, c3 = st.columns((0.2,2,0.3))
  with c2:
    m = folium.Map (location = [-15,-53], tiles=natgeo, attr='National Geographic, Esri',zoom_start =  4)   
#Escolha do período 1900
    if choose == 1900:
       folium.GeoJson(m1900, name='1900', tooltip=folium.GeoJsonTooltip(fields=['nome']),
                     style_function=lambda x: style 
       ).add_to(m)
       folium_static(m)
#Escolha do período 1910
    elif choose == 1910:
      folium.GeoJson(m1910, name='1910', tooltip=folium.GeoJsonTooltip(fields=['nome']),
                     style_function=lambda x: style1
                                              if x['properties']['nome']=='Território do Acre'
                                              else style
      ).add_to(m)
      folium_static(m)

#Escolha do período 1920
    elif choose == 1920:
      folium.GeoJson(m1920, name='1920', tooltip=folium.GeoJsonTooltip(fields=['nome']),
                    style_function=lambda x: style1
                                             if x['properties']['nome']=='Santa Catharina'
                                             else style 
      ).add_to(m)
      folium_static(m)

#Escolha do período 1930
    elif choose == 1930:
      folium.GeoJson(m1930, name='1930', tooltip=folium.GeoJsonTooltip(fields=['nome']),
                     style_function=lambda x: style
      ).add_to(m)
      folium_static(m)

#Escolha do período 1940
    elif choose == 1940:
      folium.GeoJson(m1940, name='1940', tooltip=folium.GeoJsonTooltip(fields=['nome']),
                     style_function=lambda x: style).add_to(m)
      folium.GeoJson(n1940, name='1940', tooltip=folium.GeoJsonTooltip(fields=['nome']),
                     style_function=lambda x: style1).add_to(m)
      folium_static(m)

#Escolha do período 1950
    elif choose == 1950:
      folium.GeoJson(m1950, name='1950', tooltip=folium.GeoJsonTooltip(fields=['nome']),
                     style_function=lambda x: style 
      ).add_to(m)
      folium_static(m)

#Escolha do período 1960
    elif choose == 1960:
      folium.GeoJson(m1960, name='1960', tooltip=folium.GeoJsonTooltip(fields=['nome']),
                     style_function=lambda x: style).add_to(m)
      folium.GeoJson(n1960, name='1960', tooltip=folium.GeoJsonTooltip(fields=['nome']),
                     style_function=lambda x: style1).add_to(m)
      folium_static(m)

#Escolha do período 1970
    elif choose == 1970:
      folium.GeoJson(m1970, name='1970', tooltip=folium.GeoJsonTooltip(fields=['nome']),
                     style_function=lambda x: style1
                                              if x['properties']['nome']=='Acre'
                                              else style  
      ).add_to(m)
      folium_static(m)

#Escolha do período 1980
    elif choose == 1980:
      folium.GeoJson(m1980, name='1980', tooltip=folium.GeoJsonTooltip(fields=['nome']),
                     style_function=lambda x: style).add_to(m)
      folium.GeoJson(n1980, name='1940', tooltip=folium.GeoJsonTooltip(fields=['nome']),
                     style_function=lambda x: style1).add_to(m)
      folium_static(m)

#Escolha do período 1990
    elif choose == 1990:
      folium.GeoJson(m1990, name='1990', tooltip=folium.GeoJsonTooltip(fields=['nome']),
                     style_function=lambda x: style 
      ).add_to(m)
      folium_static(m)

#Texto e fonte
  col1, col2, col3 = st.columns((0.2,1,0.3))
  with col2:
    with st.expander("Fonte:"):
      st.write("Divisão Territorial 1872 - 1990. Evolução da Divisão Territorial do Brasil. Rio de Janeiro: IBGE, [2010].")
      st.write('Disponível em:', ibge, unsafe_allow_html=True)


#Mapas históricos
elif options == "Mapas históricos":
  mapas = st.sidebar.selectbox("Selecione um século:", ("Século XVI", "Século XVII", "Século XVIII", "Século XIX"))
  st.sidebar.markdown("Para visualizar os mapas mais detalhadamente clique no link indicado na referência em “Fonte”.")
#Século XVI  
  if mapas == "Século XVI":
    st.header("Mapas históricos: Século XVI")
    col1, col2 = st.columns(2)                                    
    with col1:
      col1.subheader("Carta Náutica - 1519")
      image = "https://tile.loc.gov/image-services/iiif/service:gdc:gdcwdl:wd:l_:18:56:1:wdl_18561:T0000001/full/pct:6.25/0/default.jpg"
      st.image(image, use_column_width = True)        
      with st.expander("Fonte:"):
        st.write("Holanda, A. D., Homem, L., Manuel I, K. O. P., Reinel, J. & Reinel, P. Nautical Atlas of the World, Folio 5 Recto, Southwestern Atlantic Ocean with Brazil. 1519.") 
        link = '[Library of Congress](https://www.loc.gov/item/2021668719)'    
        st.write('Fonte:', link, unsafe_allow_html=True)  
 
      st.subheader("Linha de Tordesilhas - 1574 ")
      image = "https://www.historia-brasil.com/imagens/tratado-tordesilhas.jpg"
      st.image(image, use_column_width = True)        
      with st.expander("Fonte:"):
        st.write("Teixeita, L. Linha de Tordesilhas. Lisboa, Portugal. 1574")                                             
        link = '[Mapas históricos](https://www.historia-brasil.com/mapas/teixeira-1574.htm)'    
        st.write('Fonte:', link, unsafe_allow_html=True)                
    
    with col2:                                                    
      col2.subheader("Brasil - 1565")  
      image = "https://tile.loc.gov/image-services/iiif/service:gdc:gdcwdl:wd:l_:00:80:7:wdl_00807:cart395872/full/pct:6.25/0/default.jpg"
      st.image(image, use_column_width = True)
      with st.expander("Fonte:"):
        st.write("Gastaldi, G.; Ramusio, G. B. Brazil. Venice, Italia. 1565") 
        link = '[Library of Congress](https://www.loc.gov/item/2021668321/)'    
        st.write('Fonte:', link, unsafe_allow_html=True)  
 
      st.subheader("Brasilia - 1598 ")
      image = "https://www.historia-brasil.com/mapas/mapa/barent-langenes.jpg"
      st.image(image, use_column_width = True)        
      with st.expander("Fonte:"):
        st.write("Langenes, L. Brasilia. Middelburg, Holanda. Caert-Thresoor, 1598")                                             
        link = '[Mapas históricos](https://www.historia-brasil.com/mapas/langenes.htm)'    
        st.write('Fonte:', link, unsafe_allow_html=True)
#Século XVII                            
  elif mapas == "Século XVII":  
    st.header("Mapas históricos: Século XVII")
    col1, col2 = st.columns(2)          
    with col1:
      col1.subheader("Accuratissima Brasiliae tabula - 1630")
      image = "https://tile.loc.gov/image-services/iiif/service:gdc:gdcwdl:wd:l_:01:11:0:wdl_01110:0001_cart534563f/full/pct:6.25/0/default.jpg"
      st.image(image, use_column_width = True)        
      with st.expander("Fonte:"):
        st.write("Hondius, H. Accuratissima Brasiliae tabula. Amsterdam, Holanda 1630.") 
        link = '[Library of Congress](https://lccn.loc.gov/2021668372)'    
        st.write('Fonte:', link, unsafe_allow_html=True)  
 
      st.subheader("Le Bresil - 1656 ")
      image = "https://tile.loc.gov/image-services/iiif/service:gmd:gmd5:g5400:g5400:br000002/full/pct:12.5/0/default.jpg"
      st.image(image, use_column_width = True)        
      with st.expander("Fonte:"):
        st.write("Sanson, N.Le Bresil. Paris, 1656")                                             
        link = '[Library of Congress](https://www.loc.gov/item/2003627080/)'    
        st.write('Fonte:', link, unsafe_allow_html=True)                
    
    with col2:                                                    
      col2.subheader("Carta Náutica  - 1640")  
      image = "https://www.historia-brasil.com/mapas/mapa/carta-nautica-albernaz.jpg"
      st.image(image, use_column_width = True)
      with st.expander("Fonte:"):
        st.write("Albernaz, J.T. Carta Náutica. Portugal. 1640") 
        link = '[Mapas Históricos](https://www.historia-brasil.com/mapas/carta-nautica.htm)'    
        st.write('Fonte:', link, unsafe_allow_html=True)  
 
      st.subheader("América do Sul - 1664 ")
      image = "https://www.historia-brasil.com/imagens/america-sul-blaeu.jpg"
      st.image(image, use_column_width = True)        
      with st.expander("Fonte:"):
        st.write("Blaeu, J. Nova et accuratissima totius terrarum orbis tabula. Amsterdam, Holanda. 1664")                                             
        link = '[Mapas Históricos](https://www.historia-brasil.com/mapas/mapa-blaeu.htm)'    
        st.write('Fonte:', link, unsafe_allow_html=True)

#Século XVIII
  elif mapas == "Século XVIII":
    st.header("Mapas históricos: Século XVIII")
    col1, col2 = st.columns(2)            
    with col1:
      col1.subheader("Le Bresil - 1719")
      image = "https://tile.loc.gov/image-services/iiif/service:gmd:gmd5:g5400:g5400:br000012/full/pct:12.5/0/default.jpg"
      st.image(image, use_column_width = True)        
      with st.expander("Fonte:"):
        st.write("Fer, N. D. Le Bresil. Paris, França. 1719.") 
        link = '[Library of Congress](https://www.loc.gov/item/2003627079/)'    
        st.write('Fonte:', link, unsafe_allow_html=True)  
 
      st.subheader("Mapa dos confins do Brazil  - 1749 ")
      image = "https://www.historia-brasil.com/mapas/mapa/seculo-18.jpg"
      st.image(image, use_column_width = True)        
      with st.expander("Fonte:"):
        st.write("Carvajal y Lancaster, J.; Teles, T.S. Mapa dos confins do Brazil com as terras da Coroa de Espanha na America Meridional. 1749")                                             
        link = '[Mapas Históricos](https://www.historia-brasil.com/mapas/seculo-18.htm)'    
        st.write('Fonte:', link, unsafe_allow_html=True)                
    
    with col2:                                                    
      col2.subheader("Carta geografica del Bresil  - 1740")  
      image = "https://tile.loc.gov/image-services/iiif/service:gdc:gdcwdl:wd:l_:01:19:5:wdl_01195:cart551648/full/pct:6.25/0/default.jpg"
      st.image(image, use_column_width = True)
      with st.expander("Fonte:"):
        st.write("Albrizzi, G. B. Carta geografica del Bresil. Veneza, Italia. 1740") 
        link = '[Library of Congress](https://lccn.loc.gov/2021668384)'    
        st.write('Fonte:', link, unsafe_allow_html=True)  
 
      st.subheader("Carte de la Partie Meridionale du Bresil - 1780 ")
      image = "https://www.historia-brasil.com/mapas/mapa/mapa-raynal-bonne.jpg"
      st.image(image, use_column_width = True)        
      with st.expander("Fonte:"):
        st.write("Bonne, R.; Raynal, G.T. Carte de la Partie Meridionale du Bresil, avec les Possessions Espagnoles Voisines qui en sont à l'Ouest. Paris, França. 1780")                                             
        link = '[Mapas Históricos](https://www.historia-brasil.com/mapas/raynal-bonne.htm)'    
        st.write('Fonte:', link, unsafe_allow_html=True)

#Século XIX
  elif mapas == "Século XIX": 
    st.header("Mapas históricos: Século XIX")
    col1, col2 = st.columns(2)           
    with col1:
      col1.subheader("A map of Brazil, now called New Portugal - 1814")
      image = "https://tile.loc.gov/image-services/iiif/service:gmd:gmd5:g5400:g5400:ct000635/full/pct:25/0/default.jpg"
      st.image(image, use_column_width = True)        
      with st.expander("Fonte:"):
        st.write("Carey, M. A map of Brazil, now called New Portugal. 1814") 
        link = '[Library of Congress](https://www.loc.gov/item/2001620474/)'    
        st.write('Fonte:', link, unsafe_allow_html=True)  
 
      st.subheader("Brazil - 1846 ")
      image = "https://tile.loc.gov/image-services/iiif/service:gmd:gmd5:g5400:g5400:br000011/full/pct:25/0/default.jpg"
      st.image(image, use_column_width = True)        
      with st.expander("Fonte:"):
        st.write("Tanner, H. S. Brazil. 1846 ")                                             
        link = '[Library of Congress](https://www.loc.gov/item/2003627067/)'    
        st.write('Fonte:', link, unsafe_allow_html=True) 

      st.subheader("Physical map of Brazil - 1886 ")
      image = "https://tile.loc.gov/image-services/iiif/service:gmd:gmd5:g5401:g5401c:br000070/full/pct:25/0/default.jpg"
      st.image(image, use_column_width = True)        
      with st.expander("Fonte:"):
        st.write("Wells, J. W. & Royal Geographical Society. Physical map of Brazil. 1886 ")                                             
        link = '[Library of Congress](https://www.loc.gov/item/2003627071/)'    
        st.write('Fonte:', link, unsafe_allow_html=True)               
    
    with col2:                                                    
      col2.subheader("Nova carta do Brazil e da America portugueza - 1821")  
      image = "https://tile.loc.gov/image-services/iiif/service:gmd:gmd5:g5400:g5400:br000020/full/pct:25/0/default.jpg"
      st.image(image, use_column_width = True)
      with st.expander("Fonte:"):
        st.write("Nova carta do Brazil e da America portugueza, anno de 1821. Rio de Janeiro, Brasil. 1821") 
        link = '[Library of Congress](https://www.loc.gov/item/2003682775/)'    
        st.write('Fonte:', link, unsafe_allow_html=True)  
 
      st.subheader("Brazil - 1851 ")
      image = "https://tile.loc.gov/image-services/iiif/service:gdc:gdcwdl:wd:l_:00:04:8:wdl_00048:cart354238/full/pct:50/0/default.jpg"
      st.image(image, use_column_width = True)        
      with st.expander("Fonte:"):
        st.write("Lacey, W. E.; Rapkin, J.; Winkles, H. I. Brazil. London and New York: John Tallis & Company, 1851 ")                                             
        link = '[Library of Congress](https://www.loc.gov/item/2021668296/)'    
        st.write('Fonte:', link, unsafe_allow_html=True)

      st.subheader("Carta da republica dos Estados Unidos do Brazil - 1892 ")
      image = "https://tile.loc.gov/image-services/iiif/service:gmd:gmd5:g5400:g5400:ct000636/full/pct:12.5/0/default.jpg"
      st.image(image, use_column_width = True)        
      with st.expander("Fonte:"):
        st.write("Penha, L. J. M.; Correia, S. Carta da republica dos Estados Unidos do Brazil. Rio de Janeiro, Brasil: 1892.")                                             
        link = '[Library of Congress](https://www.loc.gov/resource/g5400.ct000636/)'    
        st.write('Fonte:', link, unsafe_allow_html=True)
