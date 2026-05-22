import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/components/Home.vue";
import Itens from "@/components/Items.vue";
import Sobre from "@/components/Sobre.vue";

Vue.use(VueRouter);

const rotas = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/itens",
    name: "Itens",
    component: Itens,
  },
  {
    path: "/sobre",
    name: "Sobre",
    component: Sobre,
  },
];

const roteador = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes: rotas,
});

export default roteador;
