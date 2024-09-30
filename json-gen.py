import json

dados = {
    "conferencias": {
        "TechXperience": {
            "nome": "TechXperience 2024",

            "descricao": '''O TechXperience é uma conferência internacional voltada para o avanço das tecnologias imersivas, como realidade aumentada (AR) e 
                            realidade virtual (VR). Especialistas e empresas líderes do setor se reúnem para discutir o impacto dessas inovações no 
                            entretenimento, na educação e na indústria. Workshops práticos e exposições interativas permitirão que os participantes 
                            experimentem as mais recentes inovações em AR e VR, além de explorar oportunidades de negócios nesse campo emergente.''',

            "tema": "Tecnologias imersivas",

            "local": "São Paulo, Brasil",

            "data_texto": "14 a 16 de março de 2024",

            "regras": '''As inscrições devem ser realizadas antecipadamente através do site oficial.
                            Participantes devem usar crachás de identificação em eventos presenciais.''',

            "premio": '''Para o projeto mais inovador apresentado, que demonstra um uso criativo e impactante de AR/VR.
                            Prêmio: Troféu + US$ 10.000 para desenvolvimento do projeto + Sessão de mentoria com líderes da indústria.''',

            "nome_foto": "pao-de-queijo.jpeg",

            "organizador": "John Carmack",
            
            "palestrantes": {
                "john":{
                    "nome_desc": "John Carmack - Co-fundador da id Software e ex-CTO da Oculus VR",

                    "desc": '''John Carmack é um dos maiores nomes em realidade virtual e jogos eletrônicos. Ele foi uma das principais figuras por trás do 
                                Oculus Rift e tem vasta experiência em inovação de hardware e software para VR.''',

                    "nome_foto": "seila.jpg"
                },

                "jaron":{
                    "nome_desc": "Jaron Lanier - Cientista da Computação, Autor e Pioneiro em Realidade Virtual",

                    "desc": '''Jaron Lanier é amplamente reconhecido como um dos pioneiros da realidade virtual. Além de ser um dos primeiros a popularizar 
                                a tecnologia VR, ele também é um crítico ativo sobre os impactos sociais da tecnologia.''',

                    "nome_foto": "seila.jpg"
                },

                "cathy":{
                    "nome_desc": "Cathy Hackl - Especialista em Futuro e Realidade Aumentada/Virtual, CEO da Futures Intelligence Group",

                    "desc": '''Conhecida como "godmother do metaverso", Cathy Hackl é uma das maiores especialistas em AR/VR e no futuro da tecnologia 
                                imersiva. Ela tem ampla experiência em estratégias digitais para grandes marcas.''',

                    "nome_foto": "seila.jpg"
                }
                
            },

            "artigo": {
                "nome": "O Impacto da Realidade Virtual na Educação Imersiva",

                "autor": "Dr. Helena Moretti, FutureTech Labs",

                "resumo": '''Este estudo explora como a realidade virtual (VR) está transformando a educação, permitindo experiências de aprendizado mais 
                                imersivas. Com a VR, alunos podem interagir com ambientes históricos, explorar conceitos científicos complexos em tempo real 
                                e participar de simulações que antes eram impossíveis no ambiente tradicional de sala de aula. Avaliamos o impacto dessa 
                                tecnologia em termos de retenção de conhecimento, engajamento e desempenho acadêmico.''',

                "intro": '''A realidade virtual tem sido aplicada em diversos setores, mas na educação ela oferece um potencial único: a capacidade de 
                                transformar a sala de aula em um ambiente tridimensional e interativo. Este estudo visa medir o impacto real da VR em cenários 
                                educacionais e entender como essas ferramentas podem ser integradas de forma eficaz no currículo acadêmico tradicional.''',

                "metodologia": '''O estudo foi realizado com 200 alunos de escolas secundárias em diferentes estados, divididos em dois grupos: um grupo exposto ao 
                                    ensino tradicional e outro utilizando VR para complementar o aprendizado de temas de biologia e história. As métricas de 
                                    avaliação incluíram testes de conhecimento, questionários de satisfação e observação de engajamento durante as aulas.''',

                "resultados": '''Os resultados indicaram que os alunos que utilizaram VR tiveram uma retenção de conhecimento vinte e cinco porcento superior, além 
                                    de demonstrarem maior engajamento durante as aulas. Os questionários também revelaram que oitenta e cinco porcento dos estudantes 
                                    prefeririam ter mais aulas utilizando essa tecnologia.''',

                "conclusao": '''A VR não apenas melhora a retenção de conhecimento, mas também aumenta o engajamento dos alunos. A implementação em larga escala 
                                desta tecnologia, porém, depende de maiores investimentos e da criação de currículos adaptados.''',

                "foto": "seila.jpg"
            }

        },

            "AIFrontiersSummit": {
            "nome": "AI Frontiers Summit 2024",

            "descricao": '''O AI Frontiers Summit reúne os maiores especialistas em inteligência artificial (IA) para discutir como essa tecnologia está 
                            moldando o futuro dos negócios. Palestras inspiradoras, painéis com líderes do setor e demonstrações ao vivo mostrarão como a IA 
                            está sendo aplicada em diversas indústrias, incluindo saúde, finanças, e-commerce e manufatura. As sessões vão desde introduções 
                            para iniciantes até debates avançados sobre ética e regulamentação em IA.''',

            "tema": "Inteligência artificial (IA)",

            "local": "Lisboa, Portugal (Evento Híbrido)",

            "data_texto": "5 a 7 de abril de 2024",

            "regras": '''As inscrições devem ser realizadas antecipadamente através do site oficial.
                            Para eventos híbridos, o link para a conferência online será enviado após a confirmação da inscrição.
                            Participantes devem usar crachás de identificação em eventos presenciais.''',

            "premio": '''Para o projeto de IA que mais impacta processos empresariais, com soluções práticas e inovadoras.
                            Prêmio: Troféu + US$ 15.000 + Parceria com uma grande empresa do setor.''',

            "nome_foto": "pao-de-queijo.jpeg",

            "organizador": "Andrew Ng",

            "palestrantes": {
                "andrew":{
                    "nome_desc": "Andrew Ng - Cofundador da Coursera e fundador da Landing AI",

                    "desc": '''Andrew Ng é uma das maiores autoridades em IA, sendo cofundador da Coursera e professor adjunto na Universidade de Stanford. 
                                Ele é conhecido por seus cursos de IA e aprendizado de máquina, e tem liderado projetos inovadores que aplicam IA em diversos 
                                setores industriais.''',

                    "nome_foto": "seila.jpg"
                },

                "fei_fei":{
                    "nome_desc": "Fei-Fei Li - Professora de Ciência da Computação na Universidade de Stanford e Cofundadora do AI4ALL",

                    "desc": '''Fei-Fei Li é uma das maiores referências no campo da visão computacional e IA, sendo a ex-diretora do laboratório de IA da 
                                Stanford. Ela é uma defensora da IA ética e da diversidade no campo da tecnologia.''',

                    "nome_foto": "seila.jpg"
                },

                "demis":{
                    "nome_desc": "Demis Hassabis - CEO e Cofundador da DeepMind",

                    "desc": '''Demis Hassabis é o cofundador da DeepMind, a empresa responsável pelo desenvolvimento do AlphaGo, uma das maiores inovações em 
                                IA. Ele é uma autoridade em inteligência artificial e aprendizado profundo.''',

                    "nome_foto": "seila.jpg"
                }
                
            },

            "artigo": {
                "nome": "Processos Logísticos",

                "autor": "Dr. Rafael Siqueira, Centro de Inovação da EuroTech",

                "resumo": '''Este estudo explora o uso de redes neurais profundas para otimizar processos logísticos em grandes cadeias de suprimentos. A aplicação 
                                de inteligência artificial (IA) tem permitido identificar ineficiências, prever demandas e reduzir custos operacionais, oferecendo 
                                uma vantagem competitiva significativa para empresas globais.''',

                "intro": '''Com o crescimento das cadeias de suprimentos globais, otimizar a logística se tornou um fator crítico de sucesso para empresas. As redes 
                            neurais profundas são uma ferramenta poderosa que, quando aplicadas corretamente, podem automatizar e melhorar a eficiência de processos 
                            logísticos. Este artigo investiga como essas tecnologias podem transformar a cadeia de suprimentos, reduzindo o tempo de entrega e 
                            custos operacionais.''',

                "metodologia": '''Utilizamos uma rede neural convolucional para analisar dados de transporte, armazenagem e demanda de três grandes empresas do setor 
                                    de logística. O algoritmo foi treinado com um conjunto de dados de cinco anos e utilizado para prever as melhores rotas de 
                                    transporte, otimizar o estoque e ajustar a demanda em tempo real.''',

                "resultados": '''Os resultados mostraram uma redução média de 18% nos custos operacionais, além de uma otimização do tempo de entrega em 12%. O 
                                    sistema também foi capaz de identificar gargalos nas operações e sugerir ajustes automáticos para mitigar o impacto desses 
                                    problemas.''',

                "conclusao": '''As redes neurais profundas demonstraram ser uma solução eficaz para melhorar processos logísticos. O próximo passo seria escalar a 
                                implementação dessas tecnologias para um número maior de empresas e setores.''',

                "foto": "seila.jpg"
            }

        },

        "CyberNext": {
            "nome": "CyberNext 2024",

            "descricao": '''A CyberNext 2024 é uma conferência voltada para os desafios e soluções em segurança cibernética e proteção de dados. Com o 
                            aumento das ameaças digitais e da complexidade das infraestruturas tecnológicas, o evento reúne profissionais de TI, 
                            especialistas em segurança e líderes empresariais para discutir as melhores práticas em cibersegurança. Serão abordados tópicos 
                            como a proteção de infraestruturas críticas, criptografia, resposta a incidentes, compliance e a gestão de riscos em ambientes 
                            corporativos.''',

            "tema": "Segurança cibernética e proteção de dados",

            "local": "Nova York, EUA",

            "data_texto": "20 a 22 de maio de 2024",

            "regras": '''As inscrições devem ser realizadas antecipadamente através do site oficial.
                            Participantes devem usar crachás de identificação em eventos presenciais.''',

            "premio": '''Reconhece a solução mais eficaz e inovadora para proteger sistemas contra ameaças digitais.
                            Prêmio: Troféu + US$ 20.000 + Licenciamento do produto em grandes corporações.''',

            "nome_foto": "pao-de-queijo.jpeg",

            "organizador": "Bruce Schneier",

            "palestrantes": {
                "bruce":{
                    "nome_desc": "Bruce Schneier - Especialista em Segurança e Criptografia, Autor e Palestrante",

                    "desc": '''Bruce Schneier é um renomado especialista em segurança da informação e criptografia, autor de vários livros sobre segurança 
                                digital. Ele é consultor de grandes empresas e governos sobre cibersegurança e privacidade.''',

                    "nome_foto": "seila.jpg"
                },

                "mikko":{
                    "nome_desc": "Mikko Hyppönen - Chefe de Pesquisa da F-Secure, Especialista em Cibersegurança",

                    "desc": '''Mikko Hyppönen é um dos maiores especialistas mundiais em malware e segurança cibernética. Ele tem décadas de experiência na 
                                proteção de sistemas contra ataques cibernéticos e é um palestrante frequente em conferências de segurança globais.''',

                    "nome_foto": "seila.jpg"
                },

                "theresa":{
                    "nome_desc": "Theresa Payton - Ex-CIO da Casa Branca, CEO da Fortalice Solutions",

                    "desc": '''Theresa Payton foi a primeira mulher a ocupar o cargo de Chief Information Officer (CIO) da Casa Branca e é atualmente CEO 
                                de uma empresa de consultoria em segurança cibernética. Ela é uma figura reconhecida no combate a crimes cibernéticos e 
                                fraude digital.''',

                    "nome_foto": "seila.jpg"
                }
                
            },

            "artigo": {
                "nome": "Criptografia Pós-Quântica para Proteção de Dados Sensíveis",

                "autor": "Dr. Alan Fischer, Instituto Internacional de Tecnologia",

                "resumo": '''Com a ameaça crescente de computadores quânticos comprometendo a segurança dos métodos criptográficos atuais, este artigo explora as 
                                abordagens da criptografia pós-quântica como solução para proteger dados sensíveis no futuro. Avaliamos várias técnicas de 
                                criptografia resistentes à computação quântica e testamos sua eficiência e aplicabilidade em sistemas atuais.''',

                "intro": '''Os avanços em computação quântica representam um grande risco para a segurança de dados. A computação quântica pode quebrar rapidamente 
                            os algoritmos criptográficos tradicionais, como RSA e ECC, usados em todo o mundo. Assim, a criptografia pós-quântica surge como uma 
                            nova fronteira na proteção de dados. Este artigo examina técnicas como criptografia baseada em reticulados e códigos de correção de 
                            erros, e seu desempenho em sistemas atuais.''',

                "metodologia": '''Foram implementados algoritmos pós-quânticos em um ambiente simulado para testar sua eficiência e capacidade de integrar-se a 
                                    sistemas de segurança já existentes. Foram avaliados aspectos como tempo de processamento, taxa de sucesso na proteção de dados 
                                    e escalabilidade. Além disso, realizamos uma análise comparativa entre as novas técnicas e os métodos tradicionais de 
                                    criptografia.''',

                "resultados": '''A criptografia baseada em reticulados apresentou um nível superior de segurança em comparação com os métodos tradicionais, com uma 
                                    taxa de sucesso de 98% na proteção contra ataques simulados de computadores quânticos. No entanto, o tempo de processamento foi 
                                    cerca de 20% maior do que o dos algoritmos tradicionais, exigindo melhorias para aplicações em larga escala.''',

                "conclusao": '''A criptografia pós-quântica é essencial para o futuro da proteção de dados, especialmente com o avanço iminente da computação 
                                quântica. Embora as técnicas apresentem desafios de eficiência, sua implementação gradual é inevitável para garantir a segurança de 
                                sistemas críticos.''',

                "foto": "seila.jpg"
            }
        },
    }
    
}

# Salvando em arquivo JSON
with open("conferencias.json", "w") as f:
    json.dump(dados, f, indent= 4)

with open("conferencias.json", "r") as f:
    dados_carregados = json.load(f)

print(dados_carregados["conferencias"]["TechXperience"]["palestrantes"]["john"]["desc"])