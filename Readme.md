# I2A2 Redes Generativas

## Descrição do desafio 01

Após escolha de um dos temas propostos, o estudante deverá realizar todo o desenvolvimento apenas por meio de prompts em alguma rede generativa pré-existente. 

Os temas propostos são:

- [x] Criar um site com 3 páginas
- [_] Criar uma nova versão da história "Chapeuzinho Vermelho"
- [_] Criar uma nova versão da fábula "A Raposa e as Uvas"

O tema escolhido para o desafio 01 foi o tema 1, criar um site com 3 páginas. 

Para que o objetivo seja considerado entregue, o estudante deverá realizar o desenvolvimento de um site com 3 páginas, sendo que cada página deverá conter:

* Página 1: Login
    * Tela com campos para nome e senha, o botão "entrar" e link "esqueci minha senha"
    * Os campos deve obrigatóriamente estar preenchidos ao se clicar no botão entrar.
    O botão entrar, redireciona para a página de produtos.
* Página 2: Lista de Produtos
    * Apresentar página com uma lista de 10 produtos (a sua escolha). A lista deve conter - id do produto, nome do produto, preço unitário, foto do produto.
* Página 3: Esqueci minha senha:
    * Apresentar página com campo para a pessoa informar o e-mail cadastrado e botão "redefinir a senha". Ao se clicar no botão "redefinir a senha", validar se o campo e-mail está preenchido. Apresentar um pop-up dizendo que o link para redefinição foi enviado para o endereço informado e redirecionar para a página de login.
* As páginas devem ser integralmente criadas utilizando o ChatGPT ou outra LLM.
* As páginas devem conter o logo de uma empresa hipotética. O logo deve ser criado por uma rede generativa de imagens (MidJourney, Dall-E, etc.)
* A linguagem de script deve ser Java Script.
* Enviar as páginas e demais elementos em um arquivo compactado no e-mail. Também enviar o link se efetuar o teste da página
* Não esqueça de incluir seu nome e e-mail.


## Ferramentas utilizadas

Todos os prompts para criação do código fonte foram gerados via Platform OpenAI (Playground) e exportados como código em Python.

Os prompts foram criados com base na metodologia de Chain Of Thought (CoT).

Os arquivos estão disponíveis na pasta [prompts/openai](prompts/openai).


Para geração da imagem da logo e das imagens dos produtos foram utilizadas duas plataformas:
* https://dreamstudio.ai/
* https://wepik.com/

Para geração das imagens dos produtos utilizamos os prompts:

* Photo Realistic Healthy Products Branding Mockups, Professional Product Photographs for Organic Green Tea

* Photo Realistic Healthy Products Branding Mockups, Professional Product Photographs for Superfood Smoothie Mix

* Photo Realistic Healthy Products Branding Mockups, Professional Product Photographs for Vegan Protein Powder

* Photo Realistic Healthy Products Branding Mockups, Professional Product Photographs for Gluten-Free Granola Bars

* Photo Realistic Healthy Products Branding Mockups, Professional Product Photographs for Organic Chia Seeds

* Photo Realistic Healthy Products Branding Mockups, Professional Product Photographs for Natural Almond Butter

* Photo Realistic Healthy Products Branding Mockups, Professional Product Photographs for Detox Herbal Tea

* Photo Realistic Healthy Products Branding Mockups, Professional Product Photographs for Organic Quinoa

* Photo Realistic Healthy Products Branding Mockups, Professional Product Photographs for Plant-Based Protein Bars

* Photo Realistic Healthy Products Branding Mockups, Professional Product Photographs for Natural Coconut Oil

Para a imagem da logo utilizamos o prompt:

* a lettermark of HealthyLife, logo, serif font, vector, simple --no realistic details (não gostei muito do resultado, mas os créditos acabaram e não consegui gerar outra imagem)



