var appModule = angular.module('appModule',['ngRoute', 'ngResource']);

appModule.config(['$routeProvider', function($routeProvider) {
	$routeProvider.
		when('/', {
			templateUrl: 'static/partials/home.html'
		}).
		when('/collections', {
			templateUrl: 'static/partials/collections.html'
		}).
		when('/members', {
			templateUrl: 'static/partials/members.html'
		}).
		otherwise({
			redirectTo: '/'
		});
}]);

appModule.factory('Member', ['$resource', function($resource){
	return $resource('/api/members/:id', {}, {
		'query': { method: 'GET', isArray: false }
	});
}])


appModule.controller("MainController", ['$scope','$http','$rootScope', function($scope,$http,$rootScope) {
	console.log("This is Organization Management Portal site.");
}]);