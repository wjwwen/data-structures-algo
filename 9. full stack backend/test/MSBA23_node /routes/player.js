const express = require('express')
const router = express.Router()
let playerNow =1
router.get('/now', (req,res)=>{
    res.send(`Player ${playerNow},your turn`)
})
router.get('/next', (req,res)=>{
    playerNow = 3-playerNow
    res.send(`Next please, Player ${playerNow}`)
})
module.exports = router
