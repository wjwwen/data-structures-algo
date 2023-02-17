const express = require('express')
const app = express()
const port = 3000
const path = require('path')

const playRouter = require('./routes/player')
app.use('/player', playRouter)

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})

app.get('/main', (req,res)=>{
    res.sendFile('index.html',{
        root: path.join(__dirname,"./")
    })
})

// For serving static HTML files
app.use(express.static("client"));
