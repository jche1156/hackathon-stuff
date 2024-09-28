/**
 * Welcome to Cloudflare Workers! This is your first worker.
 *
 * - Run `npm run dev` in your terminal to start a development server
 * - Open a browser tab at http://localhost:8787/ to see your worker in action
 * - Run `npm run deploy` to publish your worker
 *
 * Learn more at https://developers.cloudflare.com/workers/
 */

export default {
	async fetch(request, env, ctx) {
		const { path_name } = new URL(request.url);

		if (path_name === "/api/beverages") {
			const { results } = await env.DB.prepare(
				"SELECT * FROM Customers WHERE CompanyName = ?",
			)
			.bind().all();
      return Response.json(results);
		}
		return new Response(`Your request is ${JSON.stringify(env)} Call /api/beverages to see everyone who works at Bs Beverages`);
		
	},
};

