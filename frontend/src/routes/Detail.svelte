<script>
  import { params } from "svelte-spa-router";


  import { prevent_default } from "svelte/internal";

</script>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
    <script>
        import fastapi from "../lib/api";
    
        export let params = {}
        let question_id = params.question_id
        console.log('question_id:'+ question_id)
        let question = {answers:[]}
        var content = ""
    
        function get_question() {
            fastapi("get", "/api/question/detail/" + question_id, {}, (json) => {
                question = json
            })
        }
        
        function post_qnswer(event){
            event.prevent_default()
            let url = "/api/answer/create/" + question_id;
            let params = {
                content : content
            }
            fastapi('post', URL, params, (json) => {
                content = ''
                get_question()
            })
        }

        get_question()
    </script>
    
    <h1>{question.subject}</h1>
    <div>
        {question.content}
    </div>
    <ul>
        {#each question.answers as answer}
            <li>{answer.content}</li>
        {/each}
    </ul>
    <form method="post">
        <textarea rows="15"></textarea>
        <input type="submit" value="답변등록" on:click="{post_answer}">
    </form>
</body>
</html>