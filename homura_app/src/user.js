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

export default userPost
