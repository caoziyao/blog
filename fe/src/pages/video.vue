<template lang="html">
	<div class="container">
		<qui-header class="qui-header"></qui-header>
		<qui-video class="qui-header"></qui-video>
	</div>
</template>

<script>
import quiHeader from '../components/header.vue'
import quiVideo from '../components/video.vue'

export default {
	components: {
		'qui-header': quiHeader,
		'qui-video': quiVideo,
	},
}
</script>

<style lang="css">
</style>
