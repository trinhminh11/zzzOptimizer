import axios from "./customize_axios";

function WEngineService() {
  return axios.get("/wengines");
}

export { WEngineService };
