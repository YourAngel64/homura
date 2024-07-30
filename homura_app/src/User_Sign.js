import React, { useState, useEffect } from "react"
import get_CSRFToken from "./csrf_token"
import { userPost } from "./user"
import axios from "axios"

function UserSign() {
  const [email, setEmail] = useState('')
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [csrf_token, setToken] = useState('')

  useEffect(() => {
    const parse_token = async () => {
      try {
        const token = await get_CSRFToken()
        setToken(token)
      }
      catch (error) {
        console.log(error)
        setToken('')
      }

    }

    parse_token()
  }, [])

  const postUser = async (e) => {
    try {
      await userPost("http://localhost:8000/user/post/",
        {
          "email": email,
          "password": password,
          "username": username
        }, csrf_token, e);

      setUsername('')
      setPassword('')
      setEmail('')

    } catch (error) {
      console.log(error)
    }
  }

  return (
    <>
      <h1 className="text-center">User Sign Up</h1>

      <br></br>

      <div className="flex justify-center">
        <form onSubmit={postUser}>
          <input type='text' placeholder="email" name='email' value={email} onChange={(e) => { setEmail(e.target.value) }}></input>
          <br></br>
          <input type='text' placeholder="password" name="password" value={password} onChange={(e) => { setPassword(e.target.value) }}></input>
          <br></br>
          <input type='text' placeholder="username" name="username" value={username} onChange={(e) => { setUsername(e.target.value) }}></input>
          <br></br>
          <button type="submit">Create Account</button>
        </form>
      </div>

      <br></br>
      <br></br>

      <div className="text-center">
        <p>{email}</p>
        <br></br>
        <p>{password}</p>
        <br></br>
        <p>{username}</p>
        <br></br>
      </div>

    </>
  )
}

export default UserSign
