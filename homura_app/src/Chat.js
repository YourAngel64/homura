import { useEffect, useRef, useState } from "react"
import { getCookie } from "./cookie"
import { userPost, userGet } from "./user.js"
import get_CSRFToken from "./csrf_token.js"
import { useNavigate } from "react-router-dom"

const Chat = () => {
  const [chat_id, setChatID] = useState('')
  const [csrf_token, setCSRFToken] = useState('')
  const [message, setMessage] = useState('')
  const [username, setUsername] = useState('')
  const [chat_name, setChatName] = useState('')
  const [message_array, setMessageArray] = useState('')
  const [add_user, setAddUser] = useState('')

  const socket = useRef(null)
  const [updateMessage, setUpdateMessage] = useState('')

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

  //WS CODE START

  useEffect(() =>{
    if(chat_id != null && !socket.current){
      const chat_id = "ola"
      socket.current = new WebSocket(`ws://localhost:8001/ws/get/${chat_id}/`)
      socket.current.onopen = () =>{
        console.log("websocket connection successful!")
      }

      socket.current.onerror = (event) =>{
        console.log(`error : ${event}`)
        console.log(event)
      }

      socket.current.onclose = (event) =>{
        console.log('connection closed')
      }
    }

    

  }, [chat_id])

  useEffect(() => {
    if(socket.current){
      socket.current.onmessage = (event) =>{

        console.log("message recieved", event.data)

        const eventData = JSON.parse(event.data)

        if(eventData.message === "successful"){
          setUpdateMessage((prevState) => !prevState)
        }

      }
    }

    return () =>{
      if(socket.current){
        socket.current.onmessage = null;
      }
    };

  }, [socket])


  //WS CODE END

  //go back home if cookie is not found
  const GoHome = () => {
    const navigate = useNavigate()

    useEffect(() => {
      navigate('/')
    }, [])
  }

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

  //Button to go back home
  const BackHome = () => {
    const navigate = useNavigate()

    const onClick = () => {
      navigate('/')
    }

    return (
      <button onClick={onClick}>Go Back Home</button>
    )
  }

  //get messages once
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
    socket.current.send({"message": "hi"})
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


  //Add User to chat
  const addUser = (e) => {

    const add_user = async () => {
      const results = await userPost(`http://localhost:8000/message/chat/add/${chat_id}`, {
        'add_user': 'Prueba'
      }, csrf_token, e)

      console.log(results)
      console.log(results.user)
    }


    add_user()
  }

  //TODO-Update everytime message is sent to db
  //We can do this by making a request to the server every 2 seconds to check for new messages
  //Or probably is time to learn about websockets...?

  return (
    <>
      {chat_id == 'null' ? <GoHome></GoHome> : <></>}
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

      <br />

      <BackHome></BackHome>

      <br />
      <br />
      <hr />

      <input type='text' placeholder="User to add username" value={add_user} onChange={(e) => { setAddUser(e.target.value) }}></input>
      <button onClick={addUser}>Add User</button>

    </>
  )
}


export default Chat
