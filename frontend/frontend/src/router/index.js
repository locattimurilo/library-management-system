import Vue from "vue";
import VueRouter from "vue-router";
import Itens from "@/components/Items.vue";

Vue.use(VueRouter);

const rotas = [
  {
    path: "/itens",
    name: "Itens",
    component: Itens,
  },
];

const roteador = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes: rotas,
});

export default roteador;
