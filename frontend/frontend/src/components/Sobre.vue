<template>
  <div class="sobre-wrapper">
    <div class="sobre-container">

      <header class="sobre-header">
        <div class="header-label">ℹ️ Informações</div>
        <h1 class="header-title">Sobre o Projeto</h1>
        <p class="header-subtitle">Sistema de Catalogação Digital de Biblioteca</p>
      </header>

      <main class="sobre-content">

        <section class="card-projeto">
          <div class="card-icon">📚</div>
          <div class="card-body">
            <h2>Projeto Integrador em Computação I — UNIVESP</h2>
            <ul class="info-list">
              <li><span class="label">Título</span><span class="value">Implantação de um sistema de catalogação digital para organização e acesso ao acervo de uma biblioteca.</span></li>
              <li><span class="label">Parceiro</span><span class="value">Fundação Educacional São Carlos (FESC)</span></li>
              <li><span class="label">Polos</span><span class="value">Analândia e Sumaré</span></li>
              <li><span class="label">Orientadora</span><span class="value">Adriana Kaneda</span></li>
            </ul>
          </div>
        </section>

        <div class="cards-grid">

          <section class="card-item">
            <div class="card-item-icon">🎯</div>
            <h3>Objetivo</h3>
            <p>Desenvolver e implementar um modelo de catalogação digital para organizar o acervo de uma biblioteca, facilitando o acesso, controle e gestão dos materiais bibliográficos.</p>
          </section>

          <section class="card-item">
            <div class="card-item-icon">❓</div>
            <h3>Problema</h3>
            <p>Muitas bibliotecas institucionais ainda operam com sistemas manuais ou softwares desatualizados. Na FESC, o sistema atual não integra a base de dados dos alunos, gerando retrabalho e dificultando o acesso à informação.</p>
          </section>

        </div>

        <section class="card-funcionalidades">
          <div class="card-icon">✨</div>
          <div class="card-body">
            <h3>Funcionalidades</h3>
            <ul class="func-list">
              <li><span class="func-dot"></span>Visualização do acervo em tempo real</li>
              <li><span class="func-dot"></span>Cadastro de novos livros</li>
              <li><span class="func-dot"></span>Edição e atualização de informações</li>
              <li><span class="func-dot"></span>Controle de disponibilidade</li>
              <li><span class="func-dot"></span>Remoção de itens do acervo</li>
            </ul>
          </div>
        </section>

        <div class="cards-grid">

          <section class="card-item">
            <div class="card-item-icon">👥</div>
            <h3>Integrantes</h3>
            <ul class="integrantes-list">
              <li>
                <div class="avatar">R</div>
                <div>
                  <strong>Reginaldo de Godoy</strong>
                  <span>RA 24218967</span>
                </div>
              </li>
              <li>
                <div class="avatar">G</div>
                <div>
                  <strong>Geraldo Gonçalves</strong>
                  <span>RA 24210717</span>
                </div>
              </li>
            </ul>
          </section>

          <section class="card-item">
            <div class="card-item-icon">🛠️</div>
            <h3>Tecnologias</h3>
            <div class="tech-tags">
              <span v-for="tech in tecnologias" :key="tech" class="tech-tag">{{ tech }}</span>
            </div>
          </section>

        </div>

      </main>

      <footer class="sobre-footer">
        <div class="footer-actions">
          <router-link to="/" class="btn btn-outline">← Voltar para o Início</router-link>
          <router-link to="/itens" class="btn btn-primary">Acessar Biblioteca →</router-link>
        </div>
        <p class="footer-copy">© 2025 — Todos os Direitos Reservados</p>
      </footer>

    </div>
  </div>
</template>

<script>
export default {
  name: "Sobre",
  data() {
    return {
      tecnologias: ["Vue.js", "Bootstrap", "Python", "Flask", "Gunicorn", "Netlify", "Render"],
    };
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;600;700&family=DM+Serif+Display&display=swap');

/* ---------- Reset & wrapper ---------- */
.sobre-wrapper {
  min-height: 100vh;
  background: #f4f1eb;
  display: flex;
  justify-content: center;
  padding: 3rem 1rem 4rem;
  font-family: 'Sora', sans-serif;
  color: #1a1a2e;
}

.sobre-container {
  width: 100%;
  max-width: 860px;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

/* ---------- Header ---------- */
.sobre-header {
  text-align: center;
  padding: 2.5rem 1.5rem;
  background: #1a1a2e;
  border-radius: 18px;
  color: #f4f1eb;
  position: relative;
  overflow: hidden;
}

.sobre-header::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 70% 0%, rgba(99, 179, 237, 0.15) 0%, transparent 60%);
  pointer-events: none;
}

.header-label {
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #63b3ed;
  margin-bottom: 0.6rem;
}

.header-title {
  font-family: 'DM Serif Display', serif;
  font-size: clamp(2rem, 5vw, 3rem);
  font-weight: 400;
  margin: 0 0 0.4rem;
  line-height: 1.1;
}

.header-subtitle {
  font-size: 0.95rem;
  font-weight: 300;
  color: #a0aec0;
  margin: 0;
}

/* ---------- Card Projeto (destaque) ---------- */
.card-projeto {
  background: #fff;
  border-radius: 16px;
  border: 1px solid #e2ddd5;
  display: flex;
  gap: 1.2rem;
  padding: 1.8rem;
  box-shadow: 0 2px 16px rgba(0,0,0,0.05);
}

.card-icon {
  font-size: 2rem;
  line-height: 1;
  flex-shrink: 0;
  margin-top: 0.2rem;
}

.card-projeto h2 {
  font-family: 'DM Serif Display', serif;
  font-size: 1.15rem;
  font-weight: 400;
  margin: 0 0 1rem;
  color: #1a1a2e;
}

.info-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 0.55rem;
}

.info-list li {
  display: flex;
  gap: 0.7rem;
  font-size: 0.9rem;
  line-height: 1.5;
  flex-wrap: wrap;
}

.info-list .label {
  font-weight: 600;
  color: #4a5568;
  min-width: 80px;
  flex-shrink: 0;
}

.info-list .value {
  color: #2d3748;
  flex: 1;
}

/* ---------- Grid de cards ---------- */
.cards-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.2rem;
}

@media (max-width: 600px) {
  .cards-grid { grid-template-columns: 1fr; }
}

.card-item {
  background: #fff;
  border-radius: 16px;
  border: 1px solid #e2ddd5;
  padding: 1.6rem;
  box-shadow: 0 2px 16px rgba(0,0,0,0.05);
}

.card-item-icon {
  font-size: 1.5rem;
  margin-bottom: 0.6rem;
}

.card-item h3 {
  font-family: 'DM Serif Display', serif;
  font-size: 1rem;
  font-weight: 400;
  margin: 0 0 0.7rem;
  color: #1a1a2e;
}

.card-item p {
  font-size: 0.88rem;
  color: #4a5568;
  line-height: 1.65;
  margin: 0;
}

/* ---------- Funcionalidades ---------- */
.card-funcionalidades {
  background: #1a1a2e;
  border-radius: 16px;
  display: flex;
  gap: 1.2rem;
  padding: 1.8rem;
  color: #f4f1eb;
}

.card-funcionalidades h3 {
  font-family: 'DM Serif Display', serif;
  font-size: 1.1rem;
  font-weight: 400;
  margin: 0 0 1rem;
  color: #f4f1eb;
}

.func-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 0.55rem;
}

.func-list li {
  display: flex;
  align-items: center;
  gap: 0.65rem;
  font-size: 0.9rem;
  color: #cbd5e0;
}

.func-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #63b3ed;
  flex-shrink: 0;
}

/* ---------- Integrantes ---------- */
.integrantes-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}

.integrantes-list li {
  display: flex;
  align-items: center;
  gap: 0.8rem;
}

.avatar {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: #1a1a2e;
  color: #f4f1eb;
  font-size: 0.85rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.integrantes-list strong {
  display: block;
  font-size: 0.9rem;
  color: #1a1a2e;
}

.integrantes-list span {
  font-size: 0.78rem;
  color: #718096;
}

/* ---------- Tecnologias ---------- */
.tech-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 0.2rem;
}

.tech-tag {
  background: #edf2f7;
  color: #2d3748;
  font-size: 0.78rem;
  font-weight: 600;
  padding: 0.3rem 0.75rem;
  border-radius: 999px;
  letter-spacing: 0.02em;
}

/* ---------- Footer ---------- */
.sobre-footer {
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  padding-top: 0.5rem;
}

.footer-actions {
  display: flex;
  gap: 0.8rem;
  flex-wrap: wrap;
  justify-content: center;
}

.btn {
  display: inline-block;
  padding: 0.7rem 1.6rem;
  border-radius: 10px;
  font-family: 'Sora', sans-serif;
  font-size: 0.9rem;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.2s ease;
  cursor: pointer;
}

.btn-primary {
  background: #1a1a2e;
  color: #f4f1eb;
  border: 2px solid #1a1a2e;
}

.btn-primary:hover {
  background: #2d3561;
  border-color: #2d3561;
}

.btn-outline {
  background: transparent;
  color: #1a1a2e;
  border: 2px solid #1a1a2e;
}

.btn-outline:hover {
  background: #1a1a2e;
  color: #f4f1eb;
}

.footer-copy {
  font-size: 0.78rem;
  color: #a0aec0;
  margin: 0;
}
</style>
