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
            Biblioteca 📚
          </h1>
          <hr />
          <br />
          <!-- Mensagem de Alerta -->
          <b-alert variant="success" v-show="mostrarMensagem" show>{{
            mensagem
          }}</b-alert>
          <button
            type="button"
            class="btn btn-success btn-sm"
            v-b-modal.item-modal
          >
            Adicionar Item
          </button>
          <br /><br />
          <table class="table table-hover">
            <!-- Cabeçalho da Tabela -->
            <thead>
              <tr>
                <!-- Células do Cabeçalho -->
                <th scope="col">Título</th>
                <th scope="col">Gênero</th>
                <th scope="col">Disponível?</th>
                <th scope="col">Ações</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(item, index) in itens" :key="index">
                <td>{{ item.title }}</td>
                <td>{{ item.genre }}</td>
                <td>
                  <span v-if="item.available"> ✔️ </span>
                  <span v-else> ❌ </span>
                </td>
                <td>
                  <div class="btn-group" role="group">
                    <button
                      type="button"
                      class="btn btn-info btn-sm"
                      v-b-modal.item-update-modal
                      @click="editarItem(item)"
                    >
                      Atualizar
                    </button>
                    <button
                      type="button"
                      class="btn btn-danger btn-sm"
                      @click="deletarItem(item)"
                    >
                      Excluir
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
          <footer
            class="bg-primary text-white text-center"
            style="border-radius: 10px"
          >
            Direitos Autorais &copy; Todos os Direitos Reservados 2025
          </footer>
        </div>
      </div>
      <!-- Primeiro Modal -->
      <b-modal
        ref="modalAdicionarItem"
        id="item-modal"
        title="Adicionar novo item"
        hide-backdrop
        hide-footer
      >
        <b-form @submit="aoEnviar" @onreset="aoRedefinir" class="w-100">
          <b-form-group
            id="grupo-form-titulo"
            label="Título:"
            label-for="input-form-titulo"
          >
            <b-form-input
              id="input-form-titulo"
              type="text"
              v-model="formAdicionarItem.title"
              required
              placeholder="Digite o título"
            >
            </b-form-input>
          </b-form-group>
        </b-form>
        <b-form @submit="aoEnviar" @onreset="aoRedefinir" class="w-100">
          <b-form-group
            id="grupo-form-genero"
            label="Gênero:"
            label-for="input-form-genero"
          >
            <b-form-input
              id="input-form-genero"
              type="text"
              v-model="formAdicionarItem.genre"
              required
              placeholder="Digite o gênero"
            >
            </b-form-input>
          </b-form-group>
          <!-- Checkbox -->
          <b-form-group id="grupo-form-disponivel">
            <b-form-checkbox-group
              v-model="formAdicionarItem.available"
              id="form-checkboxes"
            >
              <b-form-checkbox value="true"> Disponível? </b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>

          <b-button type="submit" variant="outline-info">Enviar</b-button>
          <b-button type="reset" variant="outline-danger">Redefinir</b-button>
        </b-form>
      </b-modal>

      <!-- Segundo Modal -->
      <b-modal
        ref="modalEditarItem"
        id="item-update-modal"
        title="Atualizar"
        hide-backdrop
        hide-footer
      >
        <b-form @submit="aoEnviarAtualizacao" @reset="aoRedefinirAtualizacao" class="w-100">
          <b-form-group
            id="grupo-form-titulo-editar"
            label="Título:"
            label-for="input-form-titulo-editar"
          >
            <b-form-input
              id="input-form-titulo-editar"
              type="text"
              v-model="formEditar.title"
              required
              placeholder="Digite o título"
            >
            </b-form-input>
          </b-form-group>

          <b-form-group
            id="grupo-form-genero-editar"
            label="Gênero:"
            label-for="input-form-genero-editar"
          >
            <b-form-input
              id="input-form-genero-editar"
              type="text"
              v-model="formEditar.genre"
              required
              placeholder="Digite o gênero"
            >
            </b-form-input>
          </b-form-group>

          <b-form-group id="grupo-form-disponivel-editar">
            <b-form-checkbox-group
              v-model="formEditar.available"
              id="form-checkboxes-editar"
            >
              <b-form-checkbox value="true">Disponível?</b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>

          <b-button-group>
            <b-button type="submit" variant="outline-info">Atualizar</b-button>
            <b-button type="reset" variant="outline-danger">Cancelar</b-button>
          </b-button-group>
        </b-form>
      </b-modal>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      itens: [],
      formAdicionarItem: {
        title: "",
        genre: "",
        available: [],
      },
      formEditar: {
        id: "",
        title: "",
        genre: "",
        available: [],
      },
      mensagem: "",
      mostrarMensagem: false,
    };
  },
  methods: {
    // Função GET
    obterItens() {
      const caminho = "http://localhost:5000/itens";
      axios
        .get(caminho)
        .then((res) => {
          this.itens = res.data.items;
        })
        .catch((err) => {
          console.error(err);
        });
    },
    // Função POST
    adicionarItem(carga) {
      const caminho = "http://localhost:5000/itens";
      axios
        .post(caminho, carga)
        .then(() => {
          this.obterItens();
          this.mensagem = "Item Adicionado!";
          this.mostrarMensagem = true;
          setTimeout(() => {
            this.mostrarMensagem = false;
          }, 3000);
        })
        .catch((err) => {
          console.error(err);
          this.obterItens();
        });
    },
    inicializarFormulario() {
      this.formAdicionarItem.title = "";
      this.formAdicionarItem.genre = "";
      this.formAdicionarItem.available = [];
      this.formEditar.id = "";
      this.formEditar.title = "";
      this.formEditar.genre = "";
      this.formEditar.available = [];
    },
    aoEnviar(e) {
      e.preventDefault();
      this.$refs.modalAdicionarItem.hide();
      let disponivel = false;
      if (this.formAdicionarItem.available[0]) disponivel = true;
      const carga = {
        title: this.formAdicionarItem.title,
        genre: this.formAdicionarItem.genre,
        available: disponivel,
      };
      this.adicionarItem(carga);
      this.inicializarFormulario();
    },
    // Redefinir Modal 1
    aoRedefinir(e) {
      e.preventDefault();
      this.$refs.modalAdicionarItem.hide();
      this.inicializarFormulario();
    },
    // Enviar atualização Modal 2
    aoEnviarAtualizacao(e) {
      e.preventDefault();
      this.$refs.modalEditarItem.hide();
      let disponivel = false;
      if (this.formEditar.available[0]) disponivel = true;
      const carga = {
        title: this.formEditar.title,
        genre: this.formEditar.genre,
        available: disponivel,
      };
      this.atualizarItem(carga, this.formEditar.id);
    },
    // Cancelar Modal 2
    aoRedefinirAtualizacao(e) {
      e.preventDefault();
      this.$refs.modalAdicionarItem.hide();
      this.inicializarFormulario();
      this.obterItens();
    },
    // Atualizar item individual
    atualizarItem(carga, itemId) {
      const caminho = `http://localhost:5000/itens/${itemId}`;
      axios
        .put(caminho, carga)
        .then((res) => {
          console.log("Resposta do servidor", res.data);
          this.obterItens();
          this.mensagem = "Item Atualizado!";
          this.mostrarMensagem = true;
          setTimeout(() => {
            this.mostrarMensagem = false;
          }, 3000);
        })
        .catch((err) => {
          console.error(err);
          this.obterItens();
        });
    },
    // Excluir item individual
    removerItem(itemId) {
      const caminho = `http://localhost:5000/itens/${itemId}`;
      axios
        .delete(caminho)
        .then(() => {
          this.obterItens();
          this.mensagem = "Item Removido 🗑️!";
          this.mostrarMensagem = true;
          setTimeout(() => {
            this.mostrarMensagem = false;
          }, 3000);
        })
        .catch((err) => {
          console.error(err);
          this.obterItens();
        });
    },
    // Botão atualizar
    editarItem(item) {
      this.formEditar = item;
    },
    // Botão excluir
    deletarItem(item) {
      this.removerItem(item.id);
    },
  },
  created() {
    console.log("Componente sendo criado!");
    this.obterItens();
  }
};
</script>
