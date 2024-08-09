import axios from "./customize_axios";

function AgentsService() {
  // console.log(axios.get("/test"))
  return axios.get("/agents");
}

export { AgentsService };
