import axios from "axios";

//unused function
const setCookie = async (data, e) => {
  e.preventDefault()
  try {
    const results = await axios.post('http://localhost:8000/user/post/cookie', data, {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      withCredentials: true,

    })

    console.log(results)
    return results
  }
  catch (error) {
    console.log(error)
  }
}

const postCookie = async (cookie_name, cookie_data) => {
  try {
    const results = await axios.post(`http://localhost:8000/cookie/post/${cookie_name}`, cookie_data, {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      withCredentials: true
    })

    console.log(results)
    return results.data
  }
  catch (error) {
    console.log(error)
  }
}

const deleteCookie = async (cookie_name) => {
  try {
    const results = axios.delete(`http://localhost:8000/cookie/delete/${cookie_name}`, {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      withCredentials: true
    })

    console.log(results)
  }
  catch (error) {
    console.log(error)
  }
}

const getCookie = async (cookie_name) => {
  try {
    const results = await axios.get(`http://localhost:8000/cookie/get/${cookie_name}`, {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      withCredentials: true

    })

    console.log(results)
    return results.data
  }
  catch (error) {
    console.log(error)
  }
}


export { getCookie, postCookie, deleteCookie }
