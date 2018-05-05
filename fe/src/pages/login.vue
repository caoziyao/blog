<template lang="html">
	<div class="container">
		<qui-header class="qui-header"></qui-header>
		<div class="main">

				<div class="">
					<el-input
					  placeholder="用户姓名"
					  v-model="username"
					  clearable>
					</el-input>

				</div>
				<div class="">
					<el-input
					  placeholder="密码"
					  v-model="password"
					  clearable>
					</el-input>
				</div>

				<el-button v-on:click="login">登录</el-button>
				<el-button v-on:click="sigin">注册</el-button>

		</div>

	</div>

</template>

<script>
	import quiHeader from '../components/header.vue'
export default {
	components: {
		'qui-header': quiHeader,
	},
	data() {
	 return {
		 password: '',
		 username: '',
	 }
 	},
	methods: {
		login() {
			console.log('ssssssss')
			let password = this.password
			let username = this.username
			let url = '/api/user/login'
			let data = {
				password: password,
				username: username,
			}
			if (username === '' || password === '') {
				this.$message('用户名或密码');
				return false;
			}
			this.axios.post(url, JSON.stringify(data)).then( (res) => {
				console.log('res', res.data)
			})
			.catch( (error) => {
				console.log(error);
			});

		},
		sigin() {
			console.log('sigin')
			let password = this.password
			let username = this.username
			let url = '/api/user/sigin'
			let data = {
				password: password,
				username: username,
			}
			if (username === '' || password === '') {
				this.$message('用户名或密码');
				return false;
			}
			this.axios.post(url, JSON.stringify(data)).then( (res) => {
				console.log('res', res.data)
			})
			.catch( (error) => {
				console.log(error);
			});

		}
	},
	created() {
	},
	computed: {

	}
}
</script>

<style lang="css" scroped>

	.container {
		width: 970px;
		margin: 0 auto;
	}

</style>
