import re

# Dados personalizados
nome = "Pablo de Souza Gomes"
resumo = "Sou um desenvolvedor Full Stack com experiência em criação de soluções digitais completas — desde o front-end moderno até o back-end robusto. Tenho foco em desenvolver interfaces intuitivas, sistemas escaláveis e aplicações eficientes."
telefone = "(55) 11 95666-0506"
email = "pablosouzagomes14@gmail.com"
github = "https://github.com/pablosGomes"

# Ler o arquivo HTML original
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Atualizar título
html = html.replace('<title>Patrix, Bootstrap 5 Landing Page</title>', f'<title>{nome} - Portfólio</title>')

# Atualizar navbar
html = html.replace('<li class="nav-item"><a class="nav-link" href="#services">Services</a></li>', 
                    '<li class="nav-item"><a class="nav-link" href="#skills">Habilidades</a></li>\n          <li class="nav-item"><a class="nav-link" href="#services">Serviços</a></li>')

# Atualizar botão de contato na navbar
html = html.replace('<button type="button" class="rounded-pill btn-rounded">\n          +1 728365413\n          <span>\n            <i class="fas fa-phone-alt"></i>\n          </span>\n        </button>',
                    f'<button type="button" class="rounded-pill btn-rounded">\n          {telefone}\n          <span>\n            <i class="fas fa-phone-alt"></i>\n          </span>\n        </button>')

# Atualizar seção intro
html = html.replace('<span class="display-2--intro">Hey!, I\'m Patrick</span>',
                    f'<span class="display-2--intro">Olá! Sou {nome}</span>')

html = html.replace('<span class="display-2--description lh-base">\n            this is a multi-purpose responsive layout created with bootstrap v5. \n            (here your can place your description text)\n          </span>',
                    f'<span class="display-2--description lh-base">\n            {resumo}\n          </span>')

html = html.replace('<button type="button" class="rounded-pill btn-rounded">Get in Touch\n          <span><i class="fas fa-arrow-right"></i></span>\n        </button>',
                    '<button type="button" class="rounded-pill btn-rounded" onclick="document.getElementById(\'contact\').scrollIntoView({behavior: \'smooth\'})">Entre em Contato\n          <span><i class="fas fa-arrow-right"></i></span>\n        </button>')

# Atualizar seção de campanies
html = html.replace('<h4 class="fw-bold lead mb-3">Trusted by campanies like</h4>',
                    '<h4 class="fw-bold lead mb-3">Tecnologias que utilizo</h4>')

# Atualizar serviços
html = html.replace('<h1 class="display-3 fw-bold">Our Services</h1>',
                    '<h1 class="display-3 fw-bold">Meus Serviços</h1>')

html = html.replace('<h2 class="fw-bold text-capitalize text-center">\n            Our Services Range From Initial Design To Deployment Anywhere Anytime\n          </h2>',
                    '<h2 class="fw-bold text-capitalize text-center">\n            Desenvolvimento Full Stack de Soluções Completas\n          </h2>')

html = html.replace('<p class="fw-light">\n            Lorem ipsum dolor sit amet consectetur architecto magni, \n            dicta maxime laborum temporibus dolorem esse doloremque illo quas nisi enim molestias. \n            Tempore ducimus molestiae in dolore enim.\n          </p>',
                    '<p class="fw-light">\n            Ofereço serviços completos de desenvolvimento, desde a criação de interfaces modernas até a implementação de sistemas robustos e escaláveis. Meu objetivo é transformar ideias em projetos funcionais e impactantes.\n          </p>')

# Atualizar primeiro serviço (Front-End)
html = html.replace('<div class="icon d-block fas fa-paper-plane"></div>\n          <h3 class="display-3--title mt-1">Marketing</h3>\n          <p class="lh-lg">\n            Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi, impedit rem,\n             doloremque autem quibusdam blanditiis harum alias hic accusantium \n             maxime atque ratione magni repellat?\n          </p>',
                    '<div class="icon d-block fas fa-code"></div>\n          <h3 class="display-3--title mt-1">Desenvolvimento Front-End</h3>\n          <p class="lh-lg">\n            Criação de interfaces modernas, responsivas e performáticas usando React, Tailwind e Vite. Foco em usabilidade, design limpo e experiência fluida para o usuário final.\n          </p>', 1)

# Atualizar segundo serviço (Back-End)
html = html.replace('<div class="icon d-block fas fa-code"></div>\n          <h3 class="display-3--title mt-1">web development</h3>\n          <p class="lh-lg">\n            Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi, impedit rem,\n             doloremque autem quibusdam blanditiis harum alias hic accusantium \n             maxime atque ratione magni repellat?\n          </p>',
                    '<div class="icon d-block fas fa-server"></div>\n          <h3 class="display-3--title mt-1">Desenvolvimento Back-End</h3>\n          <p class="lh-lg">\n            Construção de APIs e sistemas sólidos com Flask e MongoDB, garantindo segurança, escalabilidade e integração eficiente entre as camadas da aplicação.\n          </p>', 1)

# Atualizar terceiro serviço (Integrações)
html = html.replace('<div class="icon d-block fas fa-cloud-upload-alt"></div>\n          <h3 class="display-3--title mt-1">cloud hosting</h3>\n          <p class="lh-lg">\n            Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi, impedit rem,\n             doloremque autem quibusdam blanditiis harum alias hic accusantium \n             maxime atque ratione magni repellat?\n          </p>',
                    '<div class="icon d-block fas fa-plug"></div>\n          <h3 class="display-3--title mt-1">Integrações e Automação</h3>\n          <p class="lh-lg">\n            Implementação de integrações com serviços externos, como gateways de pagamento (Stripe), bancos de dados e APIs personalizadas. Automatizo processos para otimizar tempo e reduzir falhas.\n          </p>', 1)

# Atualizar botões Learn more
html = html.replace('<button type="button" class="rounded-pill btn-rounded border-primary">Learn more\n            <span><i class="fas fa-arrow-right"></i></span>\n          </button>',
                    '<button type="button" class="rounded-pill btn-rounded border-primary">Saiba mais\n            <span><i class="fas fa-arrow-right"></i></span>\n          </button>')

# Atualizar seção de testimonials
html = html.replace('<h1 class="display-3 fw-bold">Testimonials</h1>',
                    '<h1 class="display-3 fw-bold">Depoimentos</h1>')

html = html.replace('<p class="lead pt-1">what our clients are saying</p>',
                    '<p class="lead pt-1">O que meus clientes dizem</p>')

# Atualizar FAQ
html = html.replace('<h1 class="display-3 fw-bold text-uppercase">faq</h1>',
                    '<h1 class="display-3 fw-bold text-uppercase">Perguntas Frequentes</h1>')

html = html.replace('<p class="lead">frequently asked questions, get knowledge befere hand</p>',
                    '<p class="lead">Dúvidas frequentes, obtenha conhecimento antecipado</p>')

# Atualizar portfolio
html = html.replace('<h1 class="display-3 fw-bold text-capitalize">Latest work</h1>',
                    '<h1 class="display-3 fw-bold text-capitalize">Meus Projetos</h1>')

html = html.replace('<p class="lead">\n        Lorem ipsum dolor sit amet consectetur adipisicing elit. Sint porro temporibus distinctio.\n      </p>',
                    '<p class="lead">\n        Conheça alguns dos projetos que desenvolvi, demonstrando minha experiência em full stack development.\n      </p>')

# Salvar o arquivo atualizado
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML atualizado com sucesso!")
