import axios from "axios";

const userPost = async (url, data, csrf_token, e) => {
  e.preventDefault()

  try {
    const results = await axios.post(url, data, {
      headers: {
        "X-CSRFToken": csrf_token,
        "Content-Type": "application/x-www-form-urlencoded"
      }
    })

    return results.data
  }
  catch (error) {
    console.log(error)
    return error
  }

}

// do userGet function
const userGet = async (url, csrf_token, e) => {
  e.preventDefault()

  try {

    const results = await axios.get(url,
      {
        "X-CSRFToken": csrf_token,
      })

    return results.data
  }
  catch (error) {
    console.log(error)
  }
}

export { userPost, userGet }
