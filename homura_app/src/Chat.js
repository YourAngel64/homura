import { useEffect, useState } from "react"
import { getCookie } from "./cookie"
import { userPost, userGet } from "./user.js"
import get_CSRFToken from "./csrf_token.js"

const Chat = () => {
  const [chat_id, setChatID] = useState('')
  const [csrf_token, setCSRFToken] = useState('')
  const [message, setMessage] = useState('')
  const [username, setUsername] = useState('')
  const [chat_name, setChatName] = useState('')
  const [message_array, setMessageArray] = useState('')

  //get cookie (chat id)
  useEffect(() => {
    const get_cookie = async () => {
      const results = await getCookie('chat_id')
      const username = await getCookie('username')
      setChatID(results.chat_id)
      setUsername(username.username)
    }

    get_cookie()
  }, [])

  //get csrf token
  useEffect(() => {
    const get_token = async () => {
      const results = await get_CSRFToken()
      setCSRFToken(results)
    }
    get_token()
  }, [])

  //get chat info
  useEffect(() => {
    const get_info = async () => {
      const result = await userGet(`http://localhost:8000/message/chat/get/${chat_id}`, csrf_token)
      setChatName(result.chat_name)
    }

    if (chat_id && csrf_token)
      get_info();

  }, [chat_id, csrf_token])

  //get messages
  useEffect(() => {
    if (chat_id) {
      const get_messages = async () => {
        const results = await userGet(`http://localhost:8000/message/get/${chat_id}`, csrf_token)
        setMessageArray(results.messages)
      }

      if (chat_id && csrf_token)
        get_messages();
    }

  }, [chat_id, csrf_token])


  //post messages
  const postMessage = (e) => {
    const post_message = async () => {
      const data = {
        'username': username,
        'message': message,
      }
      const results = await userPost(`http://localhost:8000/message/post/${chat_id}`, data, csrf_token, e)
      setMessage('')
    }

    post_message()
  }

  //Render render messages
  const RenderMessages = () => {
    if (!message_array) { return; }

    return message_array.map((value) => {
      return (
        <>
          <p>{value.username}: {value.message}</p>
          <br />
        </>
      )
    })
  }

  return (
    <>
      <h1>Welcome {username}!
        <br />  ...to {chat_name}</h1>
      <br />

      <RenderMessages></RenderMessages>

      <br />
      <div>
        <form onSubmit={postMessage}>
          <input type='text' placeholder="Message" value={message} onChange={(e) => { setMessage(e.target.value) }}></input>
          <button type="submit">Send message</button>
        </form>
      </div>

    </>
  )
}


export default Chat
