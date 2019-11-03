<template>
    <v-container>
        <v-layout>
            <v-flex>
                <v-list>
                    <v-list-item v-for="(question, i) in questions" :key="i">
                      <v-list-item-content>
                        <v-list-item-title>
                            <v-btn text rounded v-text="question.text" @click="questionDetail(question.id)"></v-btn>
                        </v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                </v-list>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    export default {
        name: "Index",
        data() {
    return {
      questions: []
    }},
     mounted() {
      this.$http
        .get(this.$baseURI)
        .then((response) => {
            let questionsArray = response.data.questions;
            questionsArray.forEach(question => {
                this.questions.push({"id": question.id, "text": question.question_text})
            })
        })
        .catch(() => {
          alert("Cannot fetch polls. Try again later.");
        });
  },
  methods: {
    questionDetail(id) {
        this.$router.push("/" + id)
    }
  }}
</script>

<style scoped>

</style>