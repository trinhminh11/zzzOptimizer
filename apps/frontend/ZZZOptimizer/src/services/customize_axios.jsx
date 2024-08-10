import axios from "axios";

const instance = axios.create({
  baseURL: "http://127.0.0.1:8000/",
});
instance.interceptors.response.use(
  function (response) {
    return response.data;
  },
  function (error) {
    return Promise.reject(error.response.data);
  }
);

export default instance;
