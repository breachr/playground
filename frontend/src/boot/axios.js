import axios from 'axios'

export default ({ Vue }) => {
  axios.defaults.baseURL = 'http://127.0.0.1:8000'
  axios.defaults.xsrfCookieName = 'csrftoken'
  axios.defaults.xsrfHeaderName = 'X-CSRFToken'
  // axios.defaults.headers.common['Authorization'] = 'tokenShit'
  // axios.defaults.headers.get['Accepts'] = 'application/json'
  Vue.prototype.$axios = axios
}
