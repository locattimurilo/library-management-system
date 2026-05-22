<template>
  <div class="jumbotron vertical-center">
    <div class="container">
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/sketchy/bootstrap.min.css"
      />
      <div class="row">
        <div class="col-sm-12">
          <h1
            class="text-center bg-info text-white"
            style="border-radius: 10px"
          >
            Sobre o Sistema ℹ️
          </h1>
          <hr />
          <br />

          <div class="card">
            <div class="card-body">
              <h4>📚 Sistema de Gerenciamento de Biblioteca</h4>
              <p>
                Este é um sistema simples para gerenciar uma coleção de livros
                de biblioteca. Permite adicionar novos itens, atualizar
                informações, visualizar a lista completa e remover itens.
              </p>

              <h5>🛠️ Tecnologias Utilizadas:</h5>
              <ul>
                <li><strong>Frontend:</strong> Vue.js + Bootstrap</li>
                <li><strong>Backend:</strong> Python + Flask</li>
                <li><strong>Hospedagem Frontend:</strong> Netlify</li>
                <li><strong>Hospedagem Backend:</strong> Render</li>
              </ul>

              <h5>✨ Funcionalidades:</h5>
              <ul>
                <li>✅ Adicionar novos livros</li>
                <li>✅ Editar livros existentes</li>
                <li>✅ Marcar disponibilidade</li>
                <li>✅ Excluir livros</li>
              </ul>
            </div>
          </div>

          <br />
          <div class="text-center">
            <router-link to="/" class="btn btn-primary">
              ← Voltar para o Início
            </router-link>
          </div>

          <br />
          <footer
            class="bg-primary text-white text-center"
            style="border-radius: 10px; padding: 10px"
          >
            Direitos Autorais &copy; Todos os Direitos Reservados 2025
          </footer>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Sobre",
};
</script>
