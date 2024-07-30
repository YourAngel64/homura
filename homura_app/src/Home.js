import React, { useState, useEffect } from "react";
import userGet from "./user.js"
import get_CSRFToken from "./csrf_token";

const Home = () => {
  const [username, setUsername] = useState('')
  const [pfp, setPfp] = useState('')
  const [csrf_token, setCSRFToken] = useState('')

  //fetchToken
  useEffect(() => {
    try {
      const fetchToken = async () => {
        const token = await get_CSRFToken()
        setCSRFToken(token)
      }

      fetchToken()
    }
    catch (error) {
      console.log(error)
      setCSRFToken('null')
    }
  }, [])

  return (
    <>
    </>
  )
}

export default Home
