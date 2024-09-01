// src/data/fieldData.tsx
import { FieldCardProps } from '../types/FieldCardTypes'; // 型をインポート

export const fieldData: FieldCardProps[] = [
	{ fieldName: '圃場1', camera: true, temperature: 25, humidity: 60, powerStatus: [true, false, true] },
	{ fieldName: '圃場2', camera: false, temperature: 22, humidity: 55, powerStatus: [false, false, true] },
	{ fieldName: '圃場3', camera: true, temperature: 28, humidity: 70, powerStatus: [true, true, false] },
	// 他の圃場データも追加可能
];
