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
            class="text-center bg-primary text-white"
            style="border-radius: 10px"
          >
            Sistema de Biblioteca 📚
          </h1>
          <hr />
          <p class="text-center lead">
            Bem-vindo! Selecione uma opção abaixo:
          </p>
          <br />

          <div class="row">
            <div class="col-md-6 mb-3">
              <div class="card text-center" style="height: 100%">
                <div class="card-body">
                  <h2>📖</h2>
                  <h4 class="card-title">Gerenciar Itens</h4>
                  <p class="card-text">
                    Adicione, edite, visualize e remova livros da biblioteca.
                  </p>
                  <router-link to="/itens" class="btn btn-primary btn-lg">
                    Acessar
                  </router-link>
                </div>
              </div>
            </div>

            <div class="col-md-6 mb-3">
              <div class="card text-center" style="height: 100%">
                <div class="card-body">
                  <h2>ℹ️</h2>
                  <h4 class="card-title">Sobre o Sistema</h4>
                  <p class="card-text">
                    Saiba mais sobre este projeto e suas funcionalidades.
                  </p>
                  <router-link to="/sobre" class="btn btn-info btn-lg">
                    Saber Mais
                  </router-link>
                </div>
              </div>
            </div>
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
  name: "Home",
};
</script>
