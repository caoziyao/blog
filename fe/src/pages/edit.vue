<template lang="html">
	<div class="container">
		<qui-header class="qui-header"></qui-header>
		<h2>{{ filename }}</h2>
		<div class="main">
			<div class="main-left">
				<div class="" v-html="noteHtml">
				</div>
			</div>
		  <div class="main-right">
				<el-input
				  type="textarea"
				  :autosize="{ minRows: 2, maxRows: 100}"
				  placeholder="请输入内容"
				  v-bind:value="noteData"
					v-on:input="updateNoteData"
					v-on:blur="saveNoteData">
				</el-input>
			</div>
		</div>

	</div>

</template>

<script>
	import quiHeader from '../components/header.vue'
	import Remarkable from 'remarkable';
export default {
	components: {
		'qui-header': quiHeader,
	},
	data() {
	 return {
		 value: '',
		 path: '',
		 filename: '',
	 }
 	},
	methods: {
		saveNoteData() {
			let value = this.value
			let path = this.path
			let url = '/api/tree/save_note'
			let data = {
				path: path,
				value: value,
			}
			if (value === '' || path === '') {
				this.$message('请输入内容');
				return false;
			}
			this.axios.post(url, JSON.stringify(data)).then( (res) => {
				let data = res.data;
				this.$store.commit('updateNoteData', value);
				let msg = `保存成功 ${path}`
				this.$message(msg);
			})
			.catch( (error) => {
				console.log(error);
			});

		},
		updateNoteData(value) {
			this.value = value
			// this.$store.commit('updateNoteData', value)
		}
	},
	created() {
		let note = this.$store.state.note
		this.value = note.content;
		this.path = note.path;
		this.filename = note.filename;
	},
	computed: {
		noteData() {
			// let data = this.$store.state.noteData
			let data = this.value;
			return data
		},
		noteHtml() {
			// let data = this.$store.state.noteData
			let data = this.value;
			let md = new Remarkable();
			let m = md.render(data)
			return m
		}
	}
}
</script>

<style lang="css">

	.container {
		width: 970px;
		margin: 0 auto;
	}
	.main {
		display: flex;
	}

	.main-left {
		position: relative;
		width: 50%;
	}

	.main-right {
		position: relative;
		width: 50%;
	}
</style>
