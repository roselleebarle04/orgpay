appModule.controller('MembersController', ['$scope','$http', function($scope,$http) {
	// $scope.students = [
	// 	{
	// 		'student_id': '2013-0038',
			
	// 		'last_name': 'Ebarle',
	// 		'first_name': 'Roselle',
	// 		'middle_initial': 'M',

	// 		'student_level': 3,
	// 		'student_major': 'BSCS',
	// 		'program_department': 'CS', 
	// 		'department_college': 'SCS',

	// 		'gender': 'F',
	// 		'registration_date': 8/4/15, 
	// 		'scholarship_description': 'Honors(B)(1.50-1.75)',
	// 		'student_permanent_address': 'Purok 5A Tambo Bayug Iligan City',
	// 	},
	// 	{
	// 		'student_id': '2013-0039',
			
	// 		'last_name': 'Vilar',
	// 		'first_name': 'Ken',
	// 		'middle_initial': 'D.',

	// 		'student_level': 3,
	// 		'student_major': 'BSCS',
	// 		'program_department': 'CS', 
	// 		'department_college': 'SCS',

	// 		'gender': 'F',
	// 		'registration_date': 8/4/15, 
	// 		'scholarship_description': 'Honors(B)(1.50-1.75)',
	// 		'student_permanent_address': 'Purok 5A Tambo Bayug Iligan City',
	// 	}
	// ]
	// console.log($scope.students);
	// $http({method: 'GET', url: 'api/members'}).success(function(data) {
	// 	console.log(data.response);
	// 	$scope.posts = data.response;
	// });

	$http.get('/api/members').then(function(response) {
		console.log(response.data['response']);
		$scope.members = []
		for (r in response.data['response']){
			member = response.data['response'][r];
			console.log(member);
			$scope.members.push(member);
		}
		console.log($scope.members);
        // for (var i = response.data.results.length - 1; i >= 0; i--) {
        //     productsData.push(response.data.results[i]);
        // };
        // if (pageNumber < response.data.pages) {
        //     pageNumber++;
        //     _getPageProducts(pageNumber);
        // } else {
        //     deferred.resolve(productsData)  ;  
        // }
    });

	console.log('This is Members Page.');
}]);