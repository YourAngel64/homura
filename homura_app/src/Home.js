import React, { useState, useEffect } from "react";
import { userGet, userPost } from "./user.js"
import get_CSRFToken from "./csrf_token";

const Home = () => {
  const [username, setUsername] = useState('')
  const [pfp, setPfp] = useState('')
  const [csrf_token, setCSRFToken] = useState('')

  const [chat_name, setChatName] = useState('')
  const [chat_description, setChatDescription] = useState('')

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

  //fetch user data with get request
  useEffect(() => {
    const GetUser = async () => {
      const results = await userGet("http://localhost:8000/user/get/", csrf_token)
      setUsername(results.username)
      setPfp(results.pfp)
    }
    GetUser()
  }, [])


  //Chat functions
  const submitChat = (e) => {
    const fetch_data = async () => {
      const results = await userPost("http://localhost:8000/message/chat/post", {
        "chat_name": chat_name,
        "users": [username],
        "users_admin": [username],
        "description": chat_description,
        "unique_id": `${chat_name}-${username}-${csrf_token.slice(0, 4)}`
      }, csrf_token, e)


      console.log(results.status)
    }

    fetch_data()
  }

  //Get Chats:
  useEffect(() => {
    const getChats = async () => {
      const results = await userGet("http://localhost:8000/message/chat/get", csrf_token)
      console.log(results)
      console.log(results.chats)
    }

    getChats()
  }, [])


  return (
    <>
      {/* 1st part - User info from user backend */}
      <p>{username}</p>
      <br />
      <p>{pfp}</p>
      <br />
      {/*2nd part - Messaging functions from message backend*/}
      <h1>Create Chat</h1>

      <form onSubmit={submitChat}>
        <input type='text' placeholder="Chat Name" name="chat_name" value={chat_name} onChange={(e) => { setChatName(e.target.value) }}></input>
        <br />
        <input type='text' placeholder="Description" name="description" value={chat_description} onChange={(e) => { setChatDescription(e.target.value) }}></input>
        <br />
        <button type="submit">Submit</button>
        <br />
      </form>
    </>
  )
}

export default Home
