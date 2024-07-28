import React, { useState, useEffect } from 'react';
import get_CSRFToken from './csrf_token';
import userPost from './user';
import { setCookie, getCookie } from './cookie.js';

function App() {
  const [csrf_token, setToken] = useState('')
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [email, setEmail] = useState('')
  const [cookie, setcookie] = useState('')

  useEffect(() => {
    const fetch_data = async () => {
      try {
        const token = await get_CSRFToken()
        setToken(token)
      }
      catch (error) {
        console.log(error)
        setToken('null')
      }
    }

    fetch_data()
  }, [])

  const postUser = async (e) => {
    try {
      const result = await userPost("http://localhost:8000/user/get/", {
        "email": email,
        "password": password
      }, csrf_token, e);

      console.log(result)
      setUsername(result.username)
      setEmail('')
      setPassword('')

      await setCookie({ 'username': result.username }, e)
    }
    catch (error) {
      console.log(error)
    }
  }

  useEffect(() => {

    const get_cookie = async () => {
      const results = await getCookie()
      setcookie(results.username)
    }

    get_cookie()
  }, [])


  return (
    <>
      <div className='flex justify-center'>
        <form onSubmit={postUser}>
          <input type="text" name='email' placeholder='email' value={email} onChange={(e) => { setEmail(e.target.value) }}></input>
          <br></br>
          <input type="text" name='password' placeholder='password' value={password} onChange={(e) => { setPassword(e.target.value) }}></input>
          <br></br>
          <button type='submit'>Login</button>
        </form>
      </div>

      <br></br>

      <h1 className='text-center'>Email:</h1>
      <br></br>
      <p className='text-center'>{email}</p>
      <br></br>
      <h1 className='text-center'>Password:</h1>
      <br></br>
      <p className='text-center'>{password}</p>
      <br></br>
      <p className='text-center'>{username != 'null' && username != '' ? `Welcome ${username}!` : ''}</p>
      <p className='text-center'>{username == 'null' ? 'User not found' : ''}</p>
      <p>{cookie}</p>
    </>
  );
}

export default App;
