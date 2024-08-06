import { useEffect, useState } from "react"
import { getCookie } from "./cookie"

//chat_id will have to be obtained by cookie :(
const Chat = () => {
  const [chat_id, setChatID] = useState('')

  useEffect(() => {
    const get_cookie = async () => {
      const results = await getCookie('chat_id')
      setChatID(results.chat_id)
    }

    get_cookie()
  }, [])
  return (
    <>
      <p>ola</p>
      <p>{chat_id}</p>
    </>
  )
}


export default Chat
