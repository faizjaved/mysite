<template>
    <v-container>
        <v-layout>
            <v-flex>
                <v-list>
                    <v-list-item>
                        <v-list-item-content>
                            <v-list-item-title class="headline">
                                {{ question.question_text }}
                            </v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                    <v-list-item v-for="(choice, n) in choices"
                                 :key="n">
                        <v-list-item-content>{{choice.choice_text}} --> {{choice.votes}} votes</v-list-item-content>
                    </v-list-item>
                    <v-btn rounded color="primary ml-5" @click="vote()">Vote Again</v-btn>
                    <v-btn rounded color="ml-5" @click="pollsHome()">Back to polls</v-btn>
                </v-list>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    export default {
        name: "Results",
        data() {
            return {
                question: {},
                choices: [],
                selectedChoice: "",
                question_id: ""
            }
        },
        mounted() {
            this.question_id = this.$route.params.id
            this.$http
                .get(this.$baseURI + this.question_id)
                .then((response) => {
                    this.question = response.data.question[0];
                    this.choices = response.data.choices
                })
                .catch(() => {
                    alert("Cannot fetch poll details. Try again later.");
                });
        },
        methods: {
            vote() {
                this.$router.push("/" + this.question_id)
            },
            pollsHome() {
                this.$router.push("/")
            }
        }
    }
</script>

<style scoped>

</style>