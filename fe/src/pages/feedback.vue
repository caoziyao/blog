<template lang="html">
	<div class="container">
		<qui-header class="qui-header"></qui-header>
		<div class="main">

				<div class="">
					<el-input
					  type="textarea"
					  :autosize="{ minRows: 2, maxRows: 10}"
					  placeholder="请输入内容"
					  v-model="emailData">
					</el-input>

				</div>
				<div class="">
					<el-input
					  placeholder="你的邮箱"
					  v-model="userEmail"
					  clearable>
					</el-input>
				</div>
				<el-button v-on:click="sendEmail">发送邮件</el-button>

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
		 emailData: '',
		 userEmail: '',
	 }
 	},
	methods: {
		sendEmail() {
			console.log('ssssssss')
			let emailData = this.emailData
			let userEmail = this.userEmail
			let url = '/api/email/send_email'
			let data = {
				emailData: emailData,
				userEmail: userEmail,
			}
			if (emailData === '' || userEmail === '') {
				this.$message('email内容');
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
