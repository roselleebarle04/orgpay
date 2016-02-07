appModule.controller('MembersController', ['$scope','$http', function($scope,$http) {
	$scope.students = [
		{
			'student_id': '2013-0038',
			
			'last_name': 'Ebarle',
			'first_name': 'Roselle',
			'middle_initial': 'M',

			'student_level': 3,
			'student_major': 'BSCS',
			'program_department': 'CS', 
			'department_college': 'SCS',

			'gender': 'F',
			'registration_date': 8/4/15, 
			'scholarship_description': 'Honors(B)(1.50-1.75)',
			'student_permanent_address': 'Purok 5A Tambo Bayug Iligan City',
		},
		{
			'student_id': '2013-0039',
			
			'last_name': 'Vilar',
			'first_name': 'Ken',
			'middle_initial': 'D.',

			'student_level': 3,
			'student_major': 'BSCS',
			'program_department': 'CS', 
			'department_college': 'SCS',

			'gender': 'F',
			'registration_date': 8/4/15, 
			'scholarship_description': 'Honors(B)(1.50-1.75)',
			'student_permanent_address': 'Purok 5A Tambo Bayug Iligan City',
		}
	]
	console.log($scope.students);
	// $http({method: 'GET', url: 'api/members'}).success(function(data) {
	// 	$scope.posts = data.response;
	// });
	console.log('This is Members Page.');
}]);