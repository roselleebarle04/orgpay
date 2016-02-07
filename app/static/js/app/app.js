var appModule = angular.module('appModule',['ngRoute']);

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

appModule.controller("MainController", ['$scope','$http','$rootScope', function($scope,$http,$rootScope) {
	console.log("This is Organization Management Portal site.");
}]);