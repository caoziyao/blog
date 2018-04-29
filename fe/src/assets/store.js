
import Vue from 'vue'
import Vuex from 'vuex';
Vue.use(Vuex);


const state={
    treeData: null,
		note: {
			content: '',
			path: '',
			filename: ''
		}
}

// $store.commit('add')"
const mutations={
    add (state) {
        // state.count++;
    },
    reduce (state) {
        // state.count--;
    },
		saveTreeData(state, data) {
			state.treeData = data
		},
		updateNoteData (state, res) {
			let content = res.content
			let path = res.path

			let note = state.note
			note.content = content
			note.path = path
			note.filename = res.filename
		},
}


export default new Vuex.Store({
  state, mutations
})
