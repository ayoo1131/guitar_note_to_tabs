//Active.js

export const active = async(jobId) => {
	try{
		const response = await fetch('/api/update-active', {
			methods: 'PUT',
			headers: { 'Content-Type': 'application/json' },
      			credentials: 'include',
			body: JSON.stringify({jobId})
		});

		const result= await response.json();

                if (!response.ok){
                        throw new Error(`HTTP error! status: ${response.status}`);
                }

                else{
                        console.log('Success: ', response.message);
                }
	}

	catch(error){
		console.error('fetch error:', error );
		return[];
	}

};
