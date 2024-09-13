import axios from "axios";
import util from "../util";

const instance = axios.create({
  baseURL: util.api_dir,
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
