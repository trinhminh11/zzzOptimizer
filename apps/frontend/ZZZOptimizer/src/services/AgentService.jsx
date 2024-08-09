import axios from "./customize_axios";

function AgentsService() {
  return axios.get("/agents");
}

export { AgentsService };
