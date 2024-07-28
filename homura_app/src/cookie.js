import axios from "axios";

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

const getCookie = async () => {
  try {
    const results = await axios.get('http://localhost:8000/user/get/cookie', {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      withCredentials: true
    })

    console.log(results)
    return results.data

  } catch (error) {
    console.log(error)
  }
}
export { setCookie, getCookie }
