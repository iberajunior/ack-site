# Site Instituto Ackler

Novo site do [Instituto Ackler](https://www.institutoackler.com.br), desenvolvido pela KROMA Studio.

HTML estático + CSS/JS compartilhados. Cursos e blog serão gerenciados depois por um painel WordPress.

## Páginas
| Arquivo | Página |
|---|---|
| index.html | Home |
| sobre.html | Sobre o Instituto |
| consultoria-excelencia-operacional.html | Consultoria em Excelência Operacional (LEAN, TPM e WCM) |
| consultoria-empresarial.html | Consultoria em Gestão Operacional |
| assessment-industrial.html | Redução de Custos · Industrial Cost & Performance Assessment |
| planejamento-estrategico.html | Planejamento Estratégico (30 dias) |
| treinamentos.html | Treinamentos In Company |
| team-building.html | Team Building |
| cursos.html | Catálogo de cursos |
| curso-especialista-melhoria-continua.html | Modelo da página do curso |
| servicos-de-rh.html | (removida em 04/11, redireciona para a consultoria) |
| perguntas-frequentes.html | FAQ |
| conteudos.html | Blog (listagem) |
| 5s-por-onde-comecar.html | Modelo de artigo |
| contato.html | Contato |

## Estrutura
- `assets/` estilos, scripts e logo usados por todas as páginas
- `_build/` scripts Python que geram as páginas internas (`python3 _build/build.py`)

## Pendências
- Links de compra de cada curso na EngagEd (Área do aluno já ligada)
- Endereços de Porto Alegre e Asunción
- Logos novos de clientes (Mars, Corbion, CHS, Vandali, Maxi Gráfica) em assets/clientes
- Confirmar endereço do escritório
- Catálogo real de cursos e fotos próprias

## Versão em espanhol (`/es/`)
- Gerada automaticamente no fim do build (`_build/es.py`) a partir das páginas em português.
- Traduções em `_build/es.json` (texto PT → texto ES). Espanhol neutro latino-americano, tratamento "usted".
- Quando um texto em PT muda, o build lista o que ficou sem tradução; basta acrescentar no `es.json` e rodar de novo.
- Seletor PT | ES na barra superior e no menu do celular, sempre apontando para a página equivalente.
