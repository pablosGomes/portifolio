import re

# Dados personalizados
nome = "Pablo de Souza Gomes"
email = "pablosouzagomes14@gmail.com"
telefone = "(55) 11 95666-0506"
github = "https://github.com/pablosGomes"

# Ler o arquivo HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ===== ATUALIZAR PORTFOLIO PROJECTS =====
# Projeto 1: RayTech AI
projeto1_html = '''<div class="portfolio-item">
              <div class="portfolio__pic">
                <img src="images/portfolio/portfolio-1.jpg" alt="RayTech AI - Website Institucional" class="img-fluid">
              </div>
              <div class="portfolio__info">
                <h3>RayTech AI – Website Institucional</h3>
                <p>Site institucional moderno com design limpo e responsivo, desenvolvido com foco em apresentação de marca e conversão. Implementado com HTML, CSS e JavaScript, mantendo alto desempenho e estética profissional.</p>
                <a href="#" class="btn btn-outline-primary">Ver Projeto</a>
              </div>
            </div>'''

# Projeto 2: Sistema de Chamados
projeto2_html = '''<div class="portfolio-item">
              <div class="portfolio__pic">
                <img src="images/portfolio/portfolio-2.jpg" alt="Sistema de Chamados LINX & ENG" class="img-fluid">
              </div>
              <div class="portfolio__info">
                <h3>Sistema de Chamados LINX & ENG</h3>
                <p>Aplicação completa de gerenciamento de chamados, com Flask no back-end e React + Tailwind no front-end. Estruturado para controle de tarefas, status e integração com banco de dados MongoDB.</p>
                <a href="#" class="btn btn-outline-primary">Ver Projeto</a>
              </div>
            </div>'''

# Projeto 3: E-Commerce com Stripe
projeto3_html = '''<div class="portfolio-item">
              <div class="portfolio__pic">
                <img src="images/portfolio/portfolio-3.jpg" alt="E-Commerce com Integração Stripe" class="img-fluid">
              </div>
              <div class="portfolio__info">
                <h3>E-Commerce com Integração Stripe</h3>
                <p>Plataforma de e-commerce moderna, com carrinho de compras dinâmico, sistema de login e integração real com Stripe para pagamentos. Desenvolvida com React, Flask e MongoDB.</p>
                <a href="#" class="btn btn-outline-primary">Ver Projeto</a>
              </div>
            </div>'''

# ===== ATUALIZAR FOOTER COM INFORMAÇÕES DE CONTATO =====

# Atualizar seção de contato do footer
html = re.sub(
    r'<h5 class="text-capitalize fw-bold">contact</h5>.*?<ul class="list-inline campany-list">.*?</ul>',
    f'''<h5 class="text-capitalize fw-bold">Contato</h5>
        <hr class="bg-white d-inline-block mb-4" style="width: 60px; height: 2px;">
        <ul class="list-inline campany-list">
          <li><a href="mailto:{email}">{email}</a></li>
          <li><a href="tel:{telefone.replace(' ', '')}">{telefone}</a></li>
          <li><a href="{github}" target="_blank">GitHub</a></li>
        </ul>''',
    html,
    flags=re.DOTALL
)

# Atualizar informações da empresa no footer
html = html.replace(
    '<h5 class="text-capitalize fw-bold">Campany name</h5>',
    f'<h5 class="text-capitalize fw-bold">{nome}</h5>'
)

html = html.replace(
    '<p class="lh-lg">\n          Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorem ex obcaecati blanditiis reprehenderit ab mollitia voluptatem consectetur?\n        </p>',
    f'<p class="lh-lg">\n          Desenvolvedor Full Stack especializado em criar soluções digitais completas, desde interfaces modernas até sistemas escaláveis. Transformando ideias em projetos funcionais e impactantes.\n        </p>'
)

# Atualizar copyright
html = html.replace(
    '&COPY; Copyright 2021 <a href="#">Company</a> | Created by <a href="http://codewithpatrick.com" target="_blank">Muriungi</a><br><br>\n\n            Distributed by <a href="http://themewagon.com" target="_blank">ThemeWagon</a>',
    f'&COPY; Copyright 2025 <a href="#">{nome}</a> | Desenvolvido com dedicação e paixão por código'
)

# Atualizar redes sociais do footer
html = re.sub(
    r'<a href="#"><i class="fab fa-facebook"></i></a>.*?<a href="#"><i class="fab fa-instagram"></i></a>',
    f'''<a href="{github}" target="_blank"><i class="fab fa-github"></i></a>
        <a href="https://linkedin.com/in/pablosouzagomes" target="_blank"><i class="fab fa-linkedin"></i></a>
        <a href="mailto:{email}"><i class="fas fa-envelope"></i></a>''',
    html,
    flags=re.DOTALL
)

# Salvar o arquivo atualizado
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Portfólio atualizado com sucesso!")
