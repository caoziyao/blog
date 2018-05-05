import axios from 'axios'

const BASE_URL = 'http://127.0.0.1:8899';
axios.defaults.baseURL = BASE_URL;

export default {axios, BASE_URL};
