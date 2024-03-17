// Need to be compiled with the option : -std=c++11

#include <iostream>
#include <chrono>
#include <cmath>

int main() {
	const int N = 1000000;
	const int M = 100000;
	int a, b, c, d;
	a = 25;
	b = 879;
	
	std::chrono::duration<double, std::milli> duration;
	std::chrono::time_point<std::chrono::high_resolution_clock> start, end;
	
    // Début du chronomètre
    start = std::chrono::high_resolution_clock::now();
    // Portion de code à mesurer
    for (int i = 0; i < N; ++i) {
        c = a + b;
    }
    // Fin du chronomètre
	end = std::chrono::high_resolution_clock::now();
    // Calcul de la durée écoulée en millisecondes
    duration = end - start;
    // Affichage du temps d'exécution
    std::cout << "Temps d'execution a+b : " << duration.count()/N * 1000 << " us" << std::endl;

    // Début du chronomètre
    start = std::chrono::high_resolution_clock::now();
    // Portion de code à mesurer
    for (int i = 0; i < N; ++i) {
        c = a * b;
    }
    // Fin du chronomètre
    end = std::chrono::high_resolution_clock::now();
    // Calcul de la durée écoulée en millisecondes
    duration = end - start;
    // Affichage du temps d'exécution
    std::cout << "Temps d'execution a*b : " << duration.count()/N * 1000 << " us" << std::endl;

    // Début du chronomètre
    start = std::chrono::high_resolution_clock::now();
    // Portion de code à mesurer
    for (int i = 0; i < N; ++i) {
        c = a * a;
    }
    // Fin du chronomètre
    end = std::chrono::high_resolution_clock::now();
    // Calcul de la durée écoulée en millisecondes
    duration = end - start;
    // Affichage du temps d'exécution
	double time_a_times_a = duration.count()/N * 1000;
    std::cout << "Temps d'execution a*a : " << time_a_times_a << " us" << std::endl;

    // Début du chronomètre
    start = std::chrono::high_resolution_clock::now();
    // Portion de code à mesurer
    for (int i = 0; i < M; ++i) {
        c = pow(a, 2);
    }
    // Fin du chronomètre
    end = std::chrono::high_resolution_clock::now();
    // Calcul de la durée écoulée en millisecondes
    duration = end - start;
    // Affichage du temps d'exécution
	double time_pow_a_2 = duration.count()/M * 1000;
    std::cout << "Temps d'execution pow(a,2) : " << time_pow_a_2 << " us" << std::endl;
	
	std::cout << "Rapport pow(a,2) / a*a : " << time_pow_a_2 / time_a_times_a << std::endl; 

    return 0;
}
