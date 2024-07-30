import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Home from './Home';
import UserLogin from './User_Login';
import UserSign from './User_Sign';
import { getCookie } from './cookie';

const App = () => {
  const [cookie, setCookie] = useState('')
  const [url, setUrl] = useState('')

  useEffect(() => {
    const fetchCookie = async () => {
      const result = await getCookie()
      console.log(result.username)
      setCookie(result.username)
    }

    fetchCookie()
  }, [])

  const checkCookie = () => {
    if (cookie != 'null') {
      return <Home />
    }

    return <UserLogin />
  }

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path='/' element={checkCookie()}></Route>
          <Route path='/sign-in' element={<UserSign />}></Route>
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App;
