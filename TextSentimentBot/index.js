'usestrict';
const express = require('express'),
      configGet=require('config');


const { TextAnalyticsClient, AzureKeyCredential} =require("@azure/ai-text-analytics");

//Azure Text Sentiment
const endpoint =configGet.get("ENDPOINT");
const apiKey=configGet.get("TEXT_ANALYTICS_API_KEY");


const app=express();

const port=process.env.PORT||process.env.port||3000;
app.listen(port,()=>{
    console.log(`listeningon${port}`);
    MS_TextSentimentAnalysis()
    .catch((err) =>{
        console.error("Error:", err);
    });
});

async function MS_TextSentimentAnalysis(thisEvent){
    console.log("[MS_TextSentimentAnalysis] in");
    const analyticsClient = new TextAnalyticsClient(endpoint, new AzureKeyCredential(apiKey));

    let documents =[];
    documents.push("我覺得櫃台人員很親切");
    const results =await analyticsClient.analyzeSentiment(documents);
    console.log("[results] ", JSON.stringify(results));
    }
