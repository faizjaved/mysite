import Vue from "vue";
import Router from "vue-router";
import Index from "@/components/Index";
import Detail from "@/components/Detail";
import Results from "@/components/Results";

Vue.use(Router);

export default new Router({
    mode: "history",
    base: process.env.BASE_URL,
    routes: [
        {
            path: "/",
            name: "index",
            component: Index
        },
        {
            path: "/:id",
            name: "detail",
            component: Detail
        },
        {
            path: "/:id/results",
            name: "results",
            component: Results
        }
    ]
})

