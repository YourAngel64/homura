import axios from "axios"
import React, { useState, useEffect } from "react"

//TODO - FETCH DATA FROM HERE U STUPID MONKEY
async function get_CSRFToken() {
  let csrf_token;

  await axios.get('http://localhost:8000/csrf_token/get/')
    .then((result) => {
      csrf_token = result.data.csrf_token
    }).catch((error) => {
      console.log(error)
      csrf_token = 'null'
    })

  return csrf_token
}

export default get_CSRFToken; 
